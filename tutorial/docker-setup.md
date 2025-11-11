# Docker Setup for Django Development

## 1. Auto-generate Docker Configuration in VS Code

The **Docker extension** in VS Code can automatically generate all necessary files for your Django project.

### Steps

1. Open your Django project in VS Code.
2. Press `Ctrl + Shift + P` to open the **Command Palette**.
3. Type `Docker` and select **“Add Docker files to workspace”**.
4. Choose **Django** as your application platform.
5. Follow the setup prompts.

After completion, VS Code will create:

* **Dockerfile** – Defines how to build the Django image.
* **docker-compose.yml** – Defines how services (web, database, etc.) interact.
* **docker-compose.debug.yml** – For debugging inside containers.
* **requirements.txt** – Lists Python dependencies.
* **.dockerignore** – Specifies files excluded from the Docker context.



## 2. Understanding the Docker Setup

### Example: `Dockerfile`

```dockerfile
# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Prevent Python from writing .pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### Example: `docker-compose.yml`

```yaml
version: "3.9"

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    environment:
      - DEBUG=1
    depends_on:
      - db

  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_USER: django
      POSTGRES_PASSWORD: django
      POSTGRES_DB: django_db
    volumes:
      - postgres_data:/var/lib/postgresql/data/

volumes:
  postgres_data:
```

### Running Containers

```bash
docker compose up --build
```

To stop all containers:

```bash
docker compose down
```



## 3. Useful Docker Compose References

* [Docker Labs Cheat Sheet](https://dockerlabs.collabnix.com/docker/cheatsheet/)
* [DevHints Docker Compose](https://devhints.io/docker-compose)
* [Jonathan Labelle Gist](https://gist.github.com/jonlabelle/bd667a97666ecda7bbc4f1cc9446d43a)



## 4. Using Docker Registry Mirrors (Proxy)

If DockerHub access is slow or blocked, you can configure **registry mirrors** to use a local or regional mirror (e.g., ArvanCloud).

### Example Configuration

```bash
sudo bash -c 'cat > /etc/docker/daemon.json <<EOF
{
  "insecure-registries" : ["https://docker.arvancloud.ir"],
  "registry-mirrors": ["https://docker.arvancloud.ir"]
}
EOF'

docker logout
sudo systemctl restart docker
```

> ⚠️ **Note:** Only use `insecure-registries` for trusted mirrors or in private environments.



## 5. Using Python (Pip) Mirrors

When installing packages via `pip`, you can use faster mirrors as an alternative to the default `pypi.org`.

### One-time Installation Example

```bash
pip install -i https://mirror-pypi.runflare.com/simple django
```

### Persistent Configuration

```bash
pip config --user set global.index https://mirror-pypi.runflare.com/simple
pip config --user set global.index-url https://mirror-pypi.runflare.com/simple
pip config --user set global.trusted-host mirror-pypi.runflare.com
```



## 6. Using Ubuntu Mirrors for Faster `apt` Updates

If your Ubuntu system fetches packages slowly, you can replace the default `apt` repositories with a regional mirror.

### Example: Sindad Mirror

```bash
sudo sed -i 's|http://[a-zA-Z0-9]*.[a-zA-Z0-9]*.*.com|http://ir.ubuntu.sindad.cloud|g' /etc/apt/sources.list
```

Then run:

```bash
sudo apt update && sudo apt upgrade
```

**Reference:** [Hostbaran – Fast Ubuntu Mirror in Iran](https://hostbaran.com/wiki/fast-speed-ubuntu-mirror-iran/)

### Example: ArvanCloud Mirror

Follow instructions from [ArvanCloud Linux Repository Guide](https://www.arvancloud.ir/fa/dev/linux-repository).
