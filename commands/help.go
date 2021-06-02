/*  Copyright (C) 2020 by Anandpskerala@Github, < https://github.com/Anandpskerala >.
 *
 * This file is part of < https://github.com/Anandpskerala/ForwardTagRemoverBot > project,
 * and is released under the "GNU v3.0 License Agreement".
 * Please see < https://github.com/Anandpskerala/ForwardTagRemoverBot/blob/master/LICENSE >
 *
 * All rights reserved.
 */

package commands

import (
	"github.com/PaulSonOfLars/gotgbot"
	"github.com/PaulSonOfLars/gotgbot/ext"
	"github.com/PaulSonOfLars/gotgbot/parsemode"
	"go.uber.org/zap"
)

func Help(b ext.Bot, u *gotgbot.Update) error {

	helpButton := [][]ext.InlineKeyboardButton{make([]ext.InlineKeyboardButton, 2), make([]ext.InlineKeyboardButton, 1)}

	helpButton[0][0] = ext.InlineKeyboardButton{
		Text: "Request",
		Url:  "https://telegram.dog/tamilmovies17_bot",
	}

	helpButton[0][1] = ext.InlineKeyboardButton{
		Text: "My Channel",
		Url:  "https://telegram.dog/Jacksparrow063",
	}

	helpButton[1][0] = ext.InlineKeyboardButton{
		Text: "Creater I'd",
		Url:  "https://www.instagram.com/invites/contact/?i=j4h4jdviuife&utm_content=ex8mxs1",
	}

	markup := ext.InlineKeyboardMarkup{InlineKeyboard: &helpButton}

	msg := b.NewSendableMessage(u.EffectiveChat.Id, "Forward Me A File,Video,Audio,Photo or Anything And \nI will Send You the File Back\n\n`How to Set Caption?`\nReply Caption to a File,Photo,Audio,Media")
	msg.ReplyToMessageId = u.EffectiveMessage.MessageId
	msg.ReplyMarkup = &markup
	msg.ParseMode = parsemode.Markdown
	_, err := msg.Send()
	if err != nil {
		b.Logger.Warnw("Error in sending", zap.Error(err))
	}
	return err
}
