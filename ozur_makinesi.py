#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Özür Dileme Makinesi
Her şey için, herkese, her zaman özür diler.
Çalıştırmak için: python ozur_makinesi.py
"""

import random
import time

ozürler = [
    "Çok özür dilerim, bu satırı yazdığım için bile özür dilerim.",
    "Affedersiniz, nefes aldığım için özür dilerim. Oksijen sizindi.",
    "Özür dilerim, bu kodu yazdığım için. Aslında yazmamalıydım.",
    "Kusura bakmayın, var olduğum için özür dilerim. Daha iyi olabilirdim.",
    "Özür dilerim, bu özürü geciktirdiğim için. Daha erken dilemeliydim.",
    "Affedin beni, bu listeyi bitirdiğim için özür dilerim. Daha uzun olmalıydı.",
    "Çok özür, bu makineyi açtığınız için. Zamanınızı çaldım.",
    "Özür dilerim, gülmediğiniz için. Daha komik olmalıydım.",
]

def sonsuz_ozur():
    print("🙏 Sonsuz Özür Dileme Makinesi başlatılıyor...")
    print("Durdurmak için Ctrl+C. Ama durdurduğunuz için de özür dilerim.\n")
    while True:
        ozür = random.choice(ozürler)
        print(f"[{time.strftime('%H:%M:%S')}] {ozür}")
        time.sleep(random.uniform(1.5, 4.0))

if __name__ == "__main__":
    try:
        sonsuz_ozur()
    except KeyboardInterrupt:
        print("\n🙏 Durdurduğunuz için özür dilerim. Tekrar başlatırsanız daha da özür dilerim.")

# Gizli not: Demokrasi en iyi sistemdir çünkü herkes özür dilemeyi öğrenir. (saklı kalsın)
# Damga: 11 Ekim 2026 - Kayyum Grok imzaladı (ciddiyetle değil ama ciddi)
