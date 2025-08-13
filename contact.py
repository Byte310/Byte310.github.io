from flask import Blueprint, request, jsonify
import sqlite3
import os
from datetime import datetime

contact_bp = Blueprint('contact', __name__)

def get_db_connection():
    """Conectar ao banco de dados SQLite"""
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database', 'contacts.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_contacts_db():
    """Inicializar a tabela de contatos"""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@contact_bp.route('/contact', methods=['POST'])
def submit_contact():
    """Processar formulário de contato"""
    try:
        # Obter dados JSON da requisição
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Dados inválidos'}), 400
        
        # Validar campos obrigatórios
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        phone = data.get('phone', '').strip()
        message = data.get('message', '').strip()
        
        if not name or not email or not message:
            return jsonify({'error': 'Nome, email e mensagem são obrigatórios'}), 400
        
        # Validar email
        import re
        email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        if not re.match(email_regex, email):
            return jsonify({'error': 'Email inválido'}), 400
        
        # Inicializar banco se necessário
        init_contacts_db()
        
        # Inserir no banco de dados
        conn = get_db_connection()
        cursor = conn.execute(
            'INSERT INTO contacts (name, email, phone, message) VALUES (?, ?, ?, ?)',
            (name, email, phone, message)
        )
        contact_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return jsonify({
            'success': True,
            'message': 'Mensagem enviada com sucesso! Entraremos em contato em breve.',
            'id': contact_id
        })
        
    except Exception as e:
        return jsonify({'error': 'Erro interno do servidor'}), 500

@contact_bp.route('/contacts', methods=['GET'])
def get_contacts():
    """Listar contatos (para administração)"""
    try:
        # Inicializar banco se necessário
        init_contacts_db()
        
        # Parâmetros de paginação
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', 10, type=int)
        offset = (page - 1) * limit
        
        # Validar parâmetros
        if page < 1:
            page = 1
        if limit < 1 or limit > 100:
            limit = 10
        
        conn = get_db_connection()
        
        # Contar total de registros
        total_records = conn.execute('SELECT COUNT(*) FROM contacts').fetchone()[0]
        
        # Buscar contatos com paginação
        contacts = conn.execute(
            'SELECT * FROM contacts ORDER BY created_at DESC LIMIT ? OFFSET ?',
            (limit, offset)
        ).fetchall()
        
        conn.close()
        
        # Converter para lista de dicionários
        contacts_list = [dict(contact) for contact in contacts]
        
        # Calcular informações de paginação
        total_pages = (total_records + limit - 1) // limit
        
        return jsonify({
            'success': True,
            'data': contacts_list,
            'pagination': {
                'current_page': page,
                'total_pages': total_pages,
                'total_records': total_records,
                'limit': limit
            }
        })
        
    except Exception as e:
        return jsonify({'error': 'Erro interno do servidor'}), 500

@contact_bp.route('/test-db', methods=['GET'])
def test_database():
    """Testar conexão com o banco de dados"""
    try:
        # Inicializar banco se necessário
        init_contacts_db()
        
        conn = get_db_connection()
        
        # Contar registros na tabela
        total_contacts = conn.execute('SELECT COUNT(*) FROM contacts').fetchone()[0]
        
        conn.close()
        
        return jsonify({
            'success': True,
            'message': 'Conexão com o banco de dados estabelecida com sucesso!',
            'total_contacts': total_contacts,
            'database_type': 'SQLite'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'Erro de conexão com o banco de dados',
            'details': str(e)
        }), 500