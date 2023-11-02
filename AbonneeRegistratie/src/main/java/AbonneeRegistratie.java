import java.io.IOException;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeoutException;

public class AbonneeRegistratie {

    CreditcardValidateClient creditcardValidateClient = new CreditcardValidateClient();
    NotificatieClient notificatieClient =  new NotificatieClient();

    public AbonneeRegistratie() throws IOException, TimeoutException {

    }

    public void nieuweAbonnee(AbonneeAanvraag aanvraag) throws IOException, ExecutionException, InterruptedException, TimeoutException {
        if(creditcardValidateClient.valideerCreditcard(aanvraag.creditcard)){
            notificatieClient.notificeerExternen();
        }
    }
}
