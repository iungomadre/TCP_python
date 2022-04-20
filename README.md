# TCP client and server

Server - prints received bytes to the console. Runs continuously until killed

Client - sends static message to address passed

## Requirements
- conda 4.10.3

## How to use
- create conda environment from requirements.txt

    ```conda create --name <env> --file requirements.txt```

- activate conda environment

    ```conda activate <env> ```

- start UDP server (will be receiving data)

    ```python udp_server.py <host_ipv4> <port> <buffer_size>```

- now datagram can be sent to the server

    ```python udp_client.py <host_ipv4> <port>```
