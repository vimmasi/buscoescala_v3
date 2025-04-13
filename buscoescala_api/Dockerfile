FROM python:3.9-slim

# Evita prompts interativos no ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=app \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=5001

# Diretório de trabalho
WORKDIR /app

# Copia o requirements e instala dependências
COPY requirements.txt .

# Atualiza pip e instala as dependências
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos
COPY . .

# Expõe a porta da API
EXPOSE 5001

# Comando padrão
CMD ["flask", "run"]
