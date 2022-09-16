<!--
    Simple static Telegram WebApp. Does not verify the WebAppInitData, as a bot token would be needed for that.
-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Avis car booking</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
</head>
<script type="text/babel">
    var form_data = "{\"class\":\"nothing selected\"}";
    function handleFormSubmit(event) {
      event.preventDefault();

      const data = new FormData(document.getElementById('formA'));

      const formJSON = Object.fromEntries(data.entries());


      form_data = JSON.stringify(formJSON, null, 2);
    }

    const form = document.querySelector('.form');
    form.addEventListener('submit', handleFormSubmit);


</script>
<script type="text/javascript">
    Telegram.WebApp.ready();
    Telegram.WebApp.MainButton.setText('Get quote').show().onClick(function () {
        const data = new FormData(document.getElementById('formA'));

        const formJSON = Object.fromEntries(data.entries());


        form_data = JSON.stringify(formJSON, null, 2);
        Telegram.WebApp.sendData(form_data);
        Telegram.WebApp.close();
    });
</script>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
:root{
  --font-light: #808080;
  --primary-color: #EB184D;
}
body{
  font-family: 'Roboto', sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 3% 0;
}
.container {
  width: 95%;
  height: 95%;
  margin: 0 auto;
}

.form{
    width: 90%;
    padding: 5%;
}
.description {
    text-transform: uppercase;
    color: var(--font-light);
    font-weight: 400;
    margin-top: 0;
}
.description strong{
  font-weight: 700;
  color: #000;
}
.description p {
    color: var(--font-light);
    font-size: 14px;
    line-height: 22px;
}
.quote p {
    font-style: italic;
    padding: 2%;
    border-left: 4px solid var(--primary-color);
}
.description ul {
    padding-left: 16px;
    list-style: circle;
}
.description ul li{
    margin: 10px 0;
}
.form{
  background: var(--primary-color);
}
.form form{
  color: var(--font-light);
    display: flex;
  flex-wrap: wrap;
}
.inpbox.full {
    width: 100%;
    background: #fff;
    padding: 3%;
    margin-bottom: 20px;
    display: flex;
    flex-wrap: wrap;
    height: 2rem ;
}
.inpbox span::before {
    margin-left: 0;
}
.inpbox span {
    padding-right: 10px;
    border-right: 2px solid var(--font-light);
}
.form select{
    border: 0;
    width: 90%;
    color: var(--font-light);
}
form input {
    border: 0;
    width: 74%;
    color: var(--font-light);
    padding: 0 4%;
}
.form select:focus, form input {
  outline: none;
}
.inpbox {
    width: 42%;
    background: #fff;
    padding: 3%;
    margin-bottom: 20px;
    margin-right: 2%;
}
.inrbox{
  width: 33%;
  color: #000;
}
.inrbox span{
  padding-right: 10px;
}
.inrbox span {
    border: 0;
    text-transform: uppercase;
    font-size: 12px;
}
.form input[type="radio"] {
    width: unset;
}
h1 {
  font-palette: light;
  text-align: center;
  color: white;
  font-size: 4rem;
}

</style>


<body>
  <div class="container">

      <div class="form">
        <h1 id="title">Cheap AVIS rentals</h1>
        <form  id="formA">
          <div class="inpbox full">
            <select id="cars" name="class">
              <option value="">Select Vehicle Class</option>
              <option value="E-Compact">Compact</option>
              <option value="E-Standard">Standard</option>
              <option value="E-Fullsize">Fullsize</option>
              <option value="F-IntermediateSUV">Intermediate SUV</option>
              <option value="G-Premium">Premium</option>
              <option value="W-StandardSUV">Standard SUV</option>
              <option value="H-Luxury">Luxury</option>
              <option value="Z-FullsizeSUV">Full size SUV</option>
            </select>
          </div>
          <div class="inpbox full">
            <span class="flaticon-globe"></span>
            <input type="text" name="pickup" maxlength="3" placeholder="Pickup Location (three letter code)">
          </div>
          <div class="inpbox">
            <input type="date" name = "pickupDate" placeholder="Pickup Date" value="2022-09-20">
          </div>
          <div class="inpbox">
            <input type="time" name = "pickupTime" step=1800 placeholder="Pickup Time" value="12:30">
          </div>
          <div class="inpbox full">
            <span class="flaticon-globe"></span>
            <input type="text" name = "Drop"  maxlength="3" placeholder="Drop Location (three letter code)">
          </div>
          <div class="inpbox">
            <input type="date" name = "DropDate" placeholder="Drop Date" value="2022-09-21">
          </div>
          <div class="inpbox">
            <input type="time" name = "DropTime" step=1800 placeholder="Drop Time" value="12:30">
          </div>
          <div class="inpbox full">
            <select id="age" name="age">
              <option value="">Select Age</option>
              <option value="25">25+</option>
              <option value="24">24</option>
              <option value="23">23</option>
              <option value="22">22</option>
              <option value="21">21</option>
              <option value="20">20</option>
            </select>
          </div>
<!--          <div class="inpbox full">-->
<!--            <div class="inrbox">-->
<!--              <span class="flaticon-taxi"> Regular</span>-->
<!--              <input type="radio" name="plan">-->
<!--              <h2>$50</h2>-->
<!--              <span>1 Passenger</span>-->
<!--            </div>-->
<!--            <div class="inrbox">-->
<!--              <span class="flaticon-taxi"> Pro</span>-->
<!--              <input type="radio" name="plan">-->
<!--              <h2>$120</h2>-->
<!--              <span>2 Passenger</span>-->
<!--            </div>-->
<!--            <div class="inrbox">-->
<!--              <span class="flaticon-taxi"> Advance</span>-->
<!--              <input type="radio" name="plan">-->
<!--              <h2>$180</h2>-->
<!--              <span>4 Passenger</span>-->
<!--            </div>-->
<!--          </div>-->
        </form>
      </div>
  </div>
</body>
<script type="text/javascript">
  Telegram.WebApp.expand();
</script>
</html>
