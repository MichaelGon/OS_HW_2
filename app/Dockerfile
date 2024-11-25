FROM ubuntu:22.04

RUN awk '{ sub(/#PermitRootLogin prohibit-password/, "PermitRootLogin yes"); } 1' /etc/ssh/sshd_config > /tmp/sshd_config \
    && mv /tmp/sshd_config /etc/ssh/sshd_config \
    && echo "root:root" | chpasswd \
    && service ssh restart

CMD ["/usr/sbin/sshd","-D"]