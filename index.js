const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
	console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg =>{
    if (msg.content === '!명령어') {
        msg.reply('1.!youtube');
    }

    if (msg.content === "!youtube") {
        msg.reply('https://www.youtube.com/channel/UCeCtNS2g3WaRrp7_QS0SaOg');
    }

})

client.login('ODM5NjQxMjQyNzAyOTcwODgw.YJMm2A.R1efWTkr8oaGD2zq9qTFLfDjKtI');