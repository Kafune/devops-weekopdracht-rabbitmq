import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeoutException;

public class AbonneeRegistratie {

    CreditcardValidateClient creditcardValidateClient = new CreditcardValidateClient();
    NotificatieClient notificatieClient = new NotificatieClient();

    public AbonneeRegistratie() throws IOException, TimeoutException, ExecutionException, InterruptedException {
        // Start listening on port 8000
        startListening(8000);
    }

    public void nieuweAbonnee(AbonneeAanvraag aanvraag) throws IOException, ExecutionException, InterruptedException, TimeoutException {
        if (creditcardValidateClient.valideerCreditcard(aanvraag.creditcard)) {
            notificatieClient.notificeerExternen();
        }
    }

    private void startListening(int port) throws ExecutionException, InterruptedException, TimeoutException {
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Listening on port " + port);
            while (true) {
                Socket clientSocket = serverSocket.accept(); // Wait for a client to connect
                System.out.println("Client connected from " + clientSocket.getInetAddress());

                try (BufferedReader reader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()))) {
                    String creditCardData = reader.readLine(); // Read the credit card data from the client

                    // Create an AbonneeAanvraag with the received credit card data
                    AbonneeAanvraag aanvraag = new AbonneeAanvraag(creditCardData);

                    // Call the nieuweAbonnee method to process the request
                    nieuweAbonnee(aanvraag);

                    clientSocket.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws IOException, TimeoutException, ExecutionException, InterruptedException {
        new AbonneeRegistratie();
    }
}
