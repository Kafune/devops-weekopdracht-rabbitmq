import com.rabbitmq.client.AMQP;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.UUID;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeoutException;

public class CreditcardValidateClient implements AutoCloseable {

    private Connection connection;
    private Channel channel;
    private String requestQueueName = "register";

    public CreditcardValidateClient() throws IOException, TimeoutException{
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");

        connection = factory.newConnection();
        channel = connection.createChannel();
    }

    public Boolean valideerCreditcard(String creditcard) throws IOException, ExecutionException, InterruptedException {
        final String corrId = UUID.randomUUID().toString();

        String replyQueueName =  channel.queueDeclare().getQueue();
        AMQP.BasicProperties props = new AMQP.BasicProperties.Builder().correlationId(corrId).replyTo(replyQueueName).build();

        channel.basicPublish("", requestQueueName, props, creditcard.getBytes(StandardCharsets.UTF_8));

        final CompletableFuture<Boolean> response = new CompletableFuture<>();

        String ctag = channel.basicConsume(replyQueueName, true, (consumerTag, delivery) -> {
            if (delivery.getProperties().getCorrelationId().equals(corrId)) {
                response.complete(Boolean.valueOf(new String(delivery.getBody(), "UTF-8")));
            }
        }, consumerTag -> {
        });

        try {
            Boolean result = response.get();
            channel.basicCancel(ctag);
            return result;
        } catch (Exception e){
            e.printStackTrace();
            return false;
        }
    }

    @Override
    public void close() throws Exception {
        connection.close();
    }
}
