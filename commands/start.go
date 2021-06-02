package commands

import (
	"fmt"

	"github.com/PaulSonOfLars/gotgbot"
	"github.com/PaulSonOfLars/gotgbot/ext"
	"github.com/PaulSonOfLars/gotgbot/parsemode"
	"go.uber.org/zap"
)

func Start(b ext.Bot, u *gotgbot.Update) error {

	startButton := [][]ext.InlineKeyboardButton{make([]ext.InlineKeyboardButton, 2), make([]ext.InlineKeyboardButton, 1)}

	startButton[0][0] = ext.InlineKeyboardButton{
		Text: "Source code",
		Url:  "https://github.com/MASTER-JD/ForwardTagRemoverBot",
	}

	startButton[0][1] = ext.InlineKeyboardButton{
		Text: "My Creater",
		Url:  "https://telegram.dog/Jacksparrow063",
	}

	startButton[1][0] = ext.InlineKeyboardButton{
		Text: "Follow On Instagram",
		Url:  "https://www.instagram.com/invites/contact/?i=or3lq84qn5za&utm_content=3tz6642",
	}

	markup := ext.InlineKeyboardMarkup{InlineKeyboard: &startButton}

	msg := b.NewSendableMessage(u.EffectiveChat.Id, fmt.Sprintf("Hi [%s](tg://user?id=%v)\nI am A Forward Tag remover Bot.Send /help To Know What I Can Do", u.EffectiveUser.FirstName, u.EffectiveUser.Id))
	msg.ReplyToMessageId = u.EffectiveMessage.MessageId
	msg.ReplyMarkup = &markup
	msg.ParseMode = parsemode.Markdown
	_, err := msg.Send()
	if err != nil {
		b.Logger.Warnw("Error in sending", zap.Error(err))
	}
	return err
}
