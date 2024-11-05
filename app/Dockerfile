FROM ubuntu:22.04

RUN apt-get update
RUN apt-get install -y python3 pip openssh-server sshpass openssh-client

RUN awk '{ sub(/#PermitRootLogin prohibit-password/, "PermitRootLogin yes"); } 1' /etc/ssh/sshd_config > /tmp/sshd_config \
    && mv /tmp/sshd_config /etc/ssh/sshd_config \
    && echo "root:root" | chpasswd \
    && service ssh restart

RUN mkdir -p /app/

COPY . app

CMD ["/usr/sbin/sshd","-D"]