import amqplib

class RabbitMQ:
    def __init__(self, RABBITMQ_HOST, RABBITMQ_PORT):
        self.connection = amqplib.connect('amqp://{}:{}'.format(RABBITMQ_HOST, RABBITMQ_PORT))
        self.channel = self.connection.channel()
    def declare_queue(self, queue_name):
        self.channel.queue_declare(queue=queue_name, durable=False)

    def publish_message(self, queue_name, message):
        self.channel.basic_publish(exchange='', routing_key=queue_name, body=message)

    def consume_messages(self, queue_name, callback):
        self.channel.basic_consume(queue=queue_name, on_message_callback=callback)

    def close(self):
        self.connection.close()
