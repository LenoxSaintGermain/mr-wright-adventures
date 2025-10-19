from flask import Blueprint, send_from_directory, jsonify
import os

downloads_bp = Blueprint('downloads', __name__)

DOCUMENTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'documents')

@downloads_bp.route('/documents', methods=['GET'])
def list_documents():
    """List all available documents"""
    try:
        files = []
        if os.path.exists(DOCUMENTS_DIR):
            for filename in os.listdir(DOCUMENTS_DIR):
                if filename.endswith('.md') or filename.endswith('.csv'):
                    files.append({
                        'filename': filename,
                        'download_url': f'/api/downloads/documents/{filename}'
                    })
        return jsonify({'documents': files}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@downloads_bp.route('/documents/<filename>', methods=['GET'])
def download_document(filename):
    """Download a specific document"""
    try:
        # Security: prevent directory traversal
        if '..' in filename or '/' in filename:
            return jsonify({'error': 'Invalid filename'}), 400
        
        if not os.path.exists(os.path.join(DOCUMENTS_DIR, filename)):
            return jsonify({'error': 'File not found'}), 404
        
        return send_from_directory(DOCUMENTS_DIR, filename, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

