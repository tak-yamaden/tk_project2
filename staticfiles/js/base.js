const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

//時間の取得
function Greetings() {
    today = new Date();
    hour = today.getHours();
//時間によってのメッセージ出力
    if ((hour >= 6) && (hour < 11)) {
        document.write('おはよう');
    } else if ((hour >= 11) && (hour < 18)) {
        document.write('こんにちは');
    } else {
        document.write('こんばんは');
    }
}
// document.querySelector('').innerHTML = Greetings();
//-->