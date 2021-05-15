from twilio.rest import Client
import smtplib


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_message(self, flight):
        self.account_sid = ''
        self.auth_token = ''
        client = Client(self.account_sid, self.auth_token)

        self.message_body = f"Low Price Alert! Only Rs.{flight['price']:,} to fly from {flight['cityFrom']}" \
                            f"-{flight['flyFrom']} to {flight['cityTo']}-{flight['flyTo']}, from " \
                            f"{flight['departureDate']} to {flight['returnDate']}"

        message = client.messages.create(
            messaging_service_sid='',
            body=self.message_body,
            to='+91-YOURNUMBER'
        )

        print(message.status)

    def send_mail(self, flight, fnames, lnames, emails):
        self.my_email = ""
        self.password = ""

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            for fname, lname, email in zip(fnames, lnames, emails):
                self.message_body = f"SUBJECT:Low Price Alert, {fname} {lname}!\n\nOnly Rs.{flight['price']:,} to fly from {flight['cityFrom']}" \
                                    f"-{flight['flyFrom']} to {flight['cityTo']}-{flight['flyTo']}, from " \
                                    f"{flight['departureDate']} to {flight['returnDate']}\n" \
                                    f"Book Here: https://www.google.co.in/flights?hl=en" \
                                    f"#flt={flight['flyFrom']}.{flight['flyTo']}.{flight['departureDate']}*" \
                                    f"{flight['flyTo']}.{flight['flyFrom']}.{flight['returnDate']}"

                print(self.message_body)
                connection.sendmail(from_addr=self.my_email,
                                    to_addrs=email,
                                    msg=self.message_body)
