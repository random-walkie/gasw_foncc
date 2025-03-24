# Scapy Development Environment
#
# SECURITY NOTE:
# This Dockerfile creates an environment with elevated network capabilities
# (NET_RAW, NET_ADMIN) which are required for Scapy to function properly for
# packet crafting and network analysis. These elevated privileges are necessary
# for development and educational purposes but reduce container isolation.
#
# This configuration is suitable for:
# - Learning network protocols
exit# - Educational environments
#
# It is NOT recommended for production deployments without additional security measures.
FROM python:3.12-bookworm

# Install system dependencies required for network tools and Scapy
RUN apt-get update && apt-get install -y \
    iputils-ping \
    tcpdump \
    wireshark \
    net-tools \
    iproute2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

WORKDIR /app

COPY /.devcontainer/requirements.txt /app
RUN pip install --requirement /app/requirements.txt --no-cache-dir

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]