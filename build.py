#!/usr/bin/env python3
# Генерирует статический сайт: политика конфиденциальности и поддержка Lumo на en/ru/es/fr.
import os, html

OUT = os.path.dirname(os.path.abspath(__file__))
ISSUES = "https://github.com/Alberto22m/lumo-privacy/issues"
EMAIL = "rnane.1@icloud.com"
DATE = {"en": "November 3, 2026", "ru": "3 ноября 2026", "es": "3 de noviembre de 2026", "fr": "3 novembre 2026"}
NAMES = {"en": "English", "ru": "Русский", "es": "Español", "fr": "Français"}

T = {
"en": dict(
  privacy_title="Lumo Privacy Policy", support_title="Lumo Support", eff="Effective",
  nav_privacy="Privacy Policy", nav_support="Support",
  privacy=[
   ("Summary", ["Lumo is a photo and video editor that works on your device. We do not collect, store on our servers, share or sell your personal data. Lumo has no accounts, no ads, no analytics and no third-party tracking."]),
   ("Photos and videos", ["Lumo asks for access to your photo library so you can choose and edit your photos and videos. You can allow full or limited access.",
     "Editing, masks, effects and exports run on your device. Your photos and videos are never uploaded to us or to anyone else. An edited photo or video is added to your library only when you choose to save or export it.",
     "To let you continue later, Lumo keeps edit settings (history, presets and recipes) on your device."]),
   ("Microphone and speech recognition", ["These are used only if you use voice input in Smart Assist. Speech is recognized on your device with Apple's on-device speech recognition. If your language is not supported on device, voice input is not offered. Audio is not recorded or sent anywhere. You can always type your request instead."]),
   ("Smart Assist", ["Text commands are interpreted on your device, using built-in rules and, where available, Apple's on-device language model. Your requests are not sent to us."]),
   ("Purchases", ["Lumo Premium is an auto-renewable subscription sold through the App Store. Apple processes the payment. We do not receive your payment details, name or Apple ID; the app only checks on your device whether your subscription is active."]),
   ("Data stored on your device", ["Language and theme settings, edit sessions, presets and recipes stay on your device. They are removed when you delete the app."]),
   ("Third parties", ["Lumo does not use third-party SDKs or services. Apple provides the App Store and iOS services under its own privacy policy."]),
   ("Children", ["Lumo is not directed to children under 13 and does not knowingly collect data from anyone."]),
   ("Your choices", ["Because we do not collect personal data, there is nothing for us to access, correct or delete. You can change or revoke access to Photos, Microphone and Speech Recognition at any time in iOS Settings > Lumo."]),
   ("Changes", ["If this policy changes, the new version will be published at this address with a new date."]),
   ("Contact", [f'Questions about privacy: write to <a href="mailto:{EMAIL}">{EMAIL}</a> or open an issue at <a href="{ISSUES}">{ISSUES}</a>. Please do not post personal information in a public issue.']),
  ],
  support=[
   ("How can I get help?", [f'Write to <a href="mailto:{EMAIL}">{EMAIL}</a> or open an issue at <a href="{ISSUES}">{ISSUES}</a> and describe the problem, your device and iOS version. Please do not include personal photos or information.']),
   ("Restore a purchase", ["Open Lumo > Settings and tap Restore Purchases. Use the same Apple ID that bought Premium."]),
   ("Manage or cancel a subscription", ["Open Lumo > Settings > Manage subscription, or iOS Settings > your name > Subscriptions. Cancel at least 24 hours before renewal."]),
   ("Where are Montage, Collage, Best shots and Video?", ["Tap the + button at the top left of the Library. You can replay the tutorial in Settings > Show tutorial."]),
   ("Lumo cannot see my photos", ["Open iOS Settings > Lumo > Photos and allow access (full or selected photos)."]),
   ("Is my data safe?", ["Everything is processed on your device and nothing is uploaded. Read the Privacy Policy for details."]),
  ]),
"ru": dict(
  privacy_title="Политика конфиденциальности Lumo", support_title="Поддержка Lumo", eff="Действует с",
  nav_privacy="Политика конфиденциальности", nav_support="Поддержка",
  privacy=[
   ("Кратко", ["Lumo — редактор фото и видео, который работает на вашем устройстве. Мы не собираем, не храним на своих серверах, не передаём и не продаём ваши персональные данные. В Lumo нет аккаунтов, рекламы, аналитики и сторонних средств отслеживания."]),
   ("Фото и видео", ["Lumo запрашивает доступ к вашей медиатеке, чтобы вы могли выбирать и редактировать фото и видео. Можно разрешить полный или ограниченный доступ.",
     "Редактирование, маски, эффекты и экспорт выполняются на вашем устройстве. Ваши фото и видео никогда не загружаются ни нам, ни кому-либо ещё. Отредактированное фото или видео добавляется в медиатеку только когда вы сами сохраняете или экспортируете его.",
     "Чтобы вы могли продолжить позже, Lumo хранит на устройстве настройки правок (историю, пресеты и рецепты)."]),
   ("Микрофон и распознавание речи", ["Они используются только при голосовом вводе в Smart Assist. Речь распознаётся на вашем устройстве встроенным распознаванием Apple. Если ваш язык не поддерживается на устройстве, голосовой ввод не предлагается. Звук не записывается и никуда не отправляется. Вместо голоса всегда можно набрать запрос текстом."]),
   ("Smart Assist", ["Текстовые команды обрабатываются на вашем устройстве встроенными правилами и, где доступно, встроенной языковой моделью Apple. Ваши запросы нам не отправляются."]),
   ("Покупки", ["Lumo Premium — подписка с автопродлением, оформляемая через App Store. Платёж обрабатывает Apple. Мы не получаем ваши платёжные данные, имя или Apple ID; приложение лишь проверяет на устройстве, активна ли подписка."]),
   ("Данные на вашем устройстве", ["Настройки языка и темы, сессии правок, пресеты и рецепты остаются на вашем устройстве. Они удаляются вместе с приложением."]),
   ("Третьи стороны", ["Lumo не использует сторонние SDK и сервисы. Apple предоставляет App Store и службы iOS в соответствии со своей политикой конфиденциальности."]),
   ("Дети", ["Lumo не предназначен для детей младше 13 лет и сознательно не собирает данные ни о ком."]),
   ("Ваш выбор", ["Поскольку мы не собираем персональные данные, у нас нечего просматривать, исправлять или удалять. Вы можете в любой момент изменить или отозвать доступ к Фото, Микрофону и Распознаванию речи в Настройках iOS > Lumo."]),
   ("Изменения", ["Если политика изменится, новая версия появится по этому адресу с новой датой."]),
   ("Контакты", [f'Вопросы о конфиденциальности: напишите на <a href="mailto:{EMAIL}">{EMAIL}</a> или создайте обращение (issue) по адресу <a href="{ISSUES}">{ISSUES}</a>. Не публикуйте личные данные в открытом обращении.']),
  ],
  support=[
   ("Как получить помощь?", [f'Напишите на <a href="mailto:{EMAIL}">{EMAIL}</a> или создайте обращение по адресу <a href="{ISSUES}">{ISSUES}</a>: опишите проблему, модель устройства и версию iOS. Не прикладывайте личные фото и данные.']),
   ("Восстановить покупку", ["Откройте Lumo > Настройки и нажмите «Восстановить покупки». Используйте тот же Apple ID, которым оформляли Premium."]),
   ("Управление и отмена подписки", ["Откройте Lumo > Настройки > Управление подпиской или Настройки iOS > ваше имя > Подписки. Отменяйте минимум за 24 часа до продления."]),
   ("Где Монтаж, Коллаж, Лучшие кадры и Видео?", ["Нажмите кнопку «+» в левом верхнем углу Библиотеки. Обучение можно открыть снова в Настройки > Показать обучение."]),
   ("Lumo не видит мои фото", ["Откройте Настройки iOS > Lumo > Фото и разрешите доступ (ко всем или к выбранным фото)."]),
   ("Мои данные в безопасности?", ["Всё обрабатывается на вашем устройстве, ничего не загружается. Подробности — в Политике конфиденциальности."]),
  ]),
"es": dict(
  privacy_title="Política de privacidad de Lumo", support_title="Soporte de Lumo", eff="En vigor desde",
  nav_privacy="Política de privacidad", nav_support="Soporte",
  privacy=[
   ("Resumen", ["Lumo es un editor de fotos y vídeos que funciona en tu dispositivo. No recopilamos, no almacenamos en nuestros servidores, no compartimos ni vendemos tus datos personales. Lumo no tiene cuentas, anuncios, analíticas ni seguimiento de terceros."]),
   ("Fotos y vídeos", ["Lumo pide acceso a tu fototeca para que puedas elegir y editar tus fotos y vídeos. Puedes permitir un acceso completo o limitado.",
     "La edición, las máscaras, los efectos y la exportación se ejecutan en tu dispositivo. Tus fotos y vídeos nunca se suben a nosotros ni a nadie más. Una foto o vídeo editado se añade a tu fototeca solo cuando decides guardarlo o exportarlo.",
     "Para que puedas continuar más tarde, Lumo guarda en tu dispositivo los ajustes de edición (historial, preajustes y recetas)."]),
   ("Micrófono y reconocimiento de voz", ["Solo se usan si utilizas la entrada de voz de Smart Assist. La voz se reconoce en tu dispositivo con el reconocimiento de voz integrado de Apple. Si tu idioma no es compatible en el dispositivo, no se ofrece la entrada de voz. El audio no se graba ni se envía a ningún sitio. Siempre puedes escribir tu petición."]),
   ("Smart Assist", ["Las órdenes de texto se interpretan en tu dispositivo con reglas integradas y, cuando está disponible, con el modelo de lenguaje de Apple en el dispositivo. Tus peticiones no se nos envían."]),
   ("Compras", ["Lumo Premium es una suscripción de renovación automática que se vende a través de la App Store. Apple procesa el pago. No recibimos tus datos de pago, tu nombre ni tu Apple ID; la app solo comprueba en tu dispositivo si tu suscripción está activa."]),
   ("Datos en tu dispositivo", ["Los ajustes de idioma y tema, las sesiones de edición, los preajustes y las recetas permanecen en tu dispositivo. Se eliminan al borrar la app."]),
   ("Terceros", ["Lumo no usa SDK ni servicios de terceros. Apple ofrece la App Store y los servicios de iOS según su propia política de privacidad."]),
   ("Menores", ["Lumo no está dirigida a menores de 13 años y no recopila datos de nadie a sabiendas."]),
   ("Tus opciones", ["Como no recopilamos datos personales, no tenemos nada que consultar, corregir o eliminar. Puedes cambiar o retirar en cualquier momento el acceso a Fotos, Micrófono y Reconocimiento de voz en Ajustes de iOS > Lumo."]),
   ("Cambios", ["Si esta política cambia, la nueva versión se publicará en esta dirección con una fecha nueva."]),
   ("Contacto", [f'Preguntas sobre privacidad: escribe a <a href="mailto:{EMAIL}">{EMAIL}</a> o abre una incidencia (issue) en <a href="{ISSUES}">{ISSUES}</a>. No publiques información personal en una incidencia pública.']),
  ],
  support=[
   ("¿Cómo puedo obtener ayuda?", [f'Escribe a <a href="mailto:{EMAIL}">{EMAIL}</a> o abre una incidencia en <a href="{ISSUES}">{ISSUES}</a> y describe el problema, tu dispositivo y la versión de iOS. No incluyas fotos ni datos personales.']),
   ("Restaurar una compra", ["Abre Lumo > Ajustes y toca Restaurar compras. Usa el mismo Apple ID con el que compraste Premium."]),
   ("Gestionar o cancelar la suscripción", ["Abre Lumo > Ajustes > Gestionar suscripción, o Ajustes de iOS > tu nombre > Suscripciones. Cancela al menos 24 horas antes de la renovación."]),
   ("¿Dónde están Montaje, Collage, Mejores tomas y Vídeo?", ["Toca el botón + de la esquina superior izquierda de la Biblioteca. Puedes repetir el tutorial en Ajustes > Mostrar tutorial."]),
   ("Lumo no ve mis fotos", ["Abre Ajustes de iOS > Lumo > Fotos y permite el acceso (a todas o a las seleccionadas)."]),
   ("¿Están seguros mis datos?", ["Todo se procesa en tu dispositivo y no se sube nada. Consulta la Política de privacidad para más detalles."]),
  ]),
"fr": dict(
  privacy_title="Politique de confidentialité de Lumo", support_title="Assistance Lumo", eff="En vigueur depuis le",
  nav_privacy="Politique de confidentialité", nav_support="Assistance",
  privacy=[
   ("En bref", ["Lumo est un éditeur de photos et de vidéos qui fonctionne sur votre appareil. Nous ne collectons pas, ne stockons pas sur nos serveurs, ne partageons pas et ne vendons pas vos données personnelles. Lumo n'a ni compte, ni publicité, ni statistiques, ni suivi par des tiers."]),
   ("Photos et vidéos", ["Lumo demande l'accès à votre photothèque pour que vous puissiez choisir et retoucher vos photos et vidéos. Vous pouvez autoriser un accès complet ou limité.",
     "La retouche, les masques, les effets et l'export s'exécutent sur votre appareil. Vos photos et vidéos ne sont jamais envoyées ni à nous ni à quiconque. Une photo ou une vidéo retouchée n'est ajoutée à votre photothèque que lorsque vous choisissez de l'enregistrer ou de l'exporter.",
     "Pour que vous puissiez reprendre plus tard, Lumo conserve sur votre appareil les réglages de retouche (historique, préréglages et recettes)."]),
   ("Micro et reconnaissance vocale", ["Ils ne sont utilisés que si vous utilisez la saisie vocale de Smart Assist. La voix est reconnue sur votre appareil par la reconnaissance vocale d'Apple. Si votre langue n'est pas prise en charge sur l'appareil, la saisie vocale n'est pas proposée. L'audio n'est ni enregistré ni envoyé. Vous pouvez toujours saisir votre demande au clavier."]),
   ("Smart Assist", ["Les commandes écrites sont interprétées sur votre appareil par des règles intégrées et, lorsqu'il est disponible, par le modèle de langage d'Apple sur l'appareil. Vos demandes ne nous sont pas envoyées."]),
   ("Achats", ["Lumo Premium est un abonnement à renouvellement automatique vendu via l'App Store. Apple traite le paiement. Nous ne recevons ni vos données de paiement, ni votre nom, ni votre identifiant Apple ; l'app vérifie seulement sur votre appareil si votre abonnement est actif."]),
   ("Données sur votre appareil", ["Les réglages de langue et de thème, les sessions de retouche, les préréglages et les recettes restent sur votre appareil. Ils sont supprimés avec l'app."]),
   ("Tiers", ["Lumo n'utilise aucun SDK ni service tiers. Apple fournit l'App Store et les services iOS selon sa propre politique de confidentialité."]),
   ("Enfants", ["Lumo ne s'adresse pas aux enfants de moins de 13 ans et ne collecte sciemment aucune donnée."]),
   ("Vos choix", ["Comme nous ne collectons aucune donnée personnelle, nous n'avons rien à consulter, corriger ou supprimer. Vous pouvez modifier ou retirer à tout moment l'accès à Photos, Micro et Reconnaissance vocale dans Réglages iOS > Lumo."]),
   ("Modifications", ["Si cette politique change, la nouvelle version sera publiée à cette adresse avec une nouvelle date."]),
   ("Contact", [f'Questions sur la confidentialité : écrivez à <a href="mailto:{EMAIL}">{EMAIL}</a> ou ouvrez un ticket (issue) sur <a href="{ISSUES}">{ISSUES}</a>. Ne publiez pas d\'informations personnelles dans un ticket public.']),
  ],
  support=[
   ("Comment obtenir de l'aide ?", [f'Écrivez à <a href="mailto:{EMAIL}">{EMAIL}</a> ou ouvrez un ticket sur <a href="{ISSUES}">{ISSUES}</a> en décrivant le problème, votre appareil et la version d\'iOS. N\'incluez ni photos ni informations personnelles.']),
   ("Restaurer un achat", ["Ouvrez Lumo > Réglages et touchez Restaurer les achats. Utilisez le même identifiant Apple que pour Premium."]),
   ("Gérer ou résilier l'abonnement", ["Ouvrez Lumo > Réglages > Gérer l'abonnement, ou Réglages iOS > votre nom > Abonnements. Résiliez au moins 24 heures avant le renouvellement."]),
   ("Où sont Montage, Collage, Meilleures photos et Vidéo ?", ["Touchez le bouton + en haut à gauche de la Photothèque. Vous pouvez revoir le tutoriel dans Réglages > Afficher le tutoriel."]),
   ("Lumo ne voit pas mes photos", ["Ouvrez Réglages iOS > Lumo > Photos et autorisez l'accès (à toutes ou aux photos sélectionnées)."]),
   ("Mes données sont-elles en sécurité ?", ["Tout est traité sur votre appareil et rien n'est envoyé. Consultez la politique de confidentialité pour les détails."]),
  ]),
}

CSS = """:root{color-scheme:light dark;--bg:#fff;--fg:#14141a;--mut:#5b5f6b;--acc:#5b6cff;--card:#f5f6fb}
@media(prefers-color-scheme:dark){:root{--bg:#0e1018;--fg:#f1f2f8;--mut:#a3a7b6;--acc:#8c96ff;--card:#181b27}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
main{max-width:760px;margin:0 auto;padding:32px 20px 64px}h1{font-size:2rem;line-height:1.2;margin:.2em 0}h2{font-size:1.25rem;margin:1.8em 0 .4em}
a{color:var(--acc)}.nav{display:flex;flex-wrap:wrap;gap:8px 16px;margin-bottom:12px}.lang{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0 20px}
.lang a{padding:4px 12px;border-radius:999px;background:var(--card);text-decoration:none;color:var(--fg)}.lang a.on{background:var(--acc);color:#fff}
.mut{color:var(--mut);font-size:.95rem}p{margin:.5em 0}"""


def page(kind, lang):
    t = T[lang]
    title = t["privacy_title"] if kind == "privacy" else t["support_title"]
    body = []
    for h, ps in t[kind]:
        body.append(f"<h2>{html.escape(h)}</h2>" + "".join(f"<p>{p}</p>" for p in ps))
    langs = "".join(f'<a href="{l}.html" class="{"on" if l == lang else ""}" hreflang="{l}">{NAMES[l]}</a>' for l in T)
    other = "support" if kind == "privacy" else "privacy"
    nav = (f'<a href="../{other}/{lang}.html">{t["nav_support"] if kind == "privacy" else t["nav_privacy"]}</a>'
           f'<a href="../index.html">Lumo</a>')
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><style>{CSS}</style></head>
<body><main><div class="nav">{nav}</div><h1>{html.escape(title)}</h1>
<div class="lang">{langs}</div>
<p class="mut">{t["eff"]}: {DATE[lang]}</p>
{''.join(body)}
</main></body></html>
"""


def index():
    rows = "".join(f'<p><b>{NAMES[l]}</b> — <a href="privacy/{l}.html">{T[l]["nav_privacy"]}</a> · <a href="support/{l}.html">{T[l]["nav_support"]}</a></p>' for l in T)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lumo</title><style>{CSS}</style></head><body><main><h1>Lumo</h1>
<p class="mut">Photo &amp; video editor for iPhone and iPad</p>{rows}</main></body></html>
"""


for kind in ("privacy", "support"):
    os.makedirs(os.path.join(OUT, kind), exist_ok=True)
    for lang in T:
        open(os.path.join(OUT, kind, f"{lang}.html"), "w", encoding="utf-8").write(page(kind, lang))
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(index())
open(os.path.join(OUT, ".nojekyll"), "w").write("")
open(os.path.join(OUT, "README.md"), "w", encoding="utf-8").write(
    "# Lumo: privacy policy and support\n\nStatic pages for the Lumo iOS app (en, ru, es, fr).\n\n"
    "- Privacy Policy: `privacy/<lang>.html`\n- Support: `support/<lang>.html`\n\nRegenerate with `python3 build.py`.\n")
print("built")
