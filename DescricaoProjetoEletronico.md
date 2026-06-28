# DK-01
## Defusal Kit 01

**Versão:** V1.0.0 (Em desenvolvimento)

**Autor:** Fabio Alves Lima / ChatGPT

**Objetivo**

Desenvolver um equipamento eletrônico portátil de alta confiabilidade para jogos de Paintball, Airsoft, Laser Tag e Simulações Militares, utilizando ESP32-S3 como controlador principal.

---

# Status do Projeto

| Fase | Descrição | Status |
|-------|-----------|--------|
| 1 | Engenharia do Sistema | 🟢 Em desenvolvimento |
| 2 | Esquemático KiCad | ⚪ Não iniciado |
| 3 | PCB Principal | ⚪ Não iniciado |
| 4 | PCB das Portas | ⚪ Não iniciado |
| 5 | PCB Display | ⚪ Não iniciado |
| 6 | Firmware Base | ⚪ Não iniciado |
| 7 | Interface LVGL | ⚪ Não iniciado |
| 8 | Protótipo | ⚪ Não iniciado |
| 9 | Produção | ⚪ Não iniciado |

---

# Objetivos

## Funcionais

O equipamento deverá suportar diversos modos de jogo.

Entre eles:

- Bomb Defusal
- Bomb Plant
- Domination
- King of the Hill
- Capture the Flag
- VIP Escort
- Search and Destroy
- Sabotage
- Treinamentos militares
- Eventos personalizados

Todos os modos deverão ser configuráveis por firmware.

---

# Objetivos de Engenharia

- Alta confiabilidade
- Fácil manutenção
- Baixo consumo
- Alta autonomia
- Atualização OTA
- USB-C
- PCB profissional
- Produção em escala

---

# Arquitetura Geral

```
                    DISPLAY
                       │
                 FFC 50 vias
                       │
                       │
             ┌─────────────────┐
             │                 │
             │   MAIN BOARD    │
             │                 │
             │ ESP32-S3        │
             │ RTC             │
             │ Áudio           │
             │ Haptic          │
             │ Power           │
             │ USB             │
             │ RGB             │
             │ Battery         │
             │                 │
             └─────────────────┘
```

---

# Placa Principal

## Geometria

Formato:

Hexágono Regular

Distância entre faces:

100 mm

Espessura:

1.6 mm

PCB:

4 camadas

Cor:

Preta

Acabamento:

ENIG

Material:

FR4 TG170

---

# Display

Tipo:

TFT IPS

Formato:

Circular

Tamanho:

2.1"

Resolução:

480x480

Controlador:

ST7701S

Interface:

RGB

Comunicação:

FFC

Quantidade de vias:

50

Passo:

0.5 mm

Backlight:

PWM

Montagem:

PCB própria instalada em uma face frontal do poliedro.

---

# Microcontrolador Principal

Modelo escolhido

ESP32-S3-WROOM-1-N16R16

Características

- Dual Core
- WiFi
- Bluetooth LE
- USB OTG
- 16MB Flash
- 16MB PSRAM

---

# Alimentação

Fonte principal

Bateria Li-Ion

Modelo

18650

Configuração

1S2P

Faixa operacional

3.0V

até

4.2V

Carregamento

USB-C

Power Path

Sim

Proteções

- Curto
- Sobrecarga
- Sobredescarga
- Temperatura

---

# Barramentos

SPI

- Display
- Flash

I²C

- RTC
- Haptic
- Sensores
- Expansores

I²S

- Áudio

USB

- Programação
- CDC
- MSC
- OTA

---

# Interface do Usuário

Display TFT

Áudio

Motor vibratório

LEDs RGB

Botões

---

# LEDs

Quantidade

36

Distribuição

3 LEDs por porta

Tipo

SK6812 Mini-E

Alimentação

5V

Controle

Barramento serial

---

# Portas

Quantidade

12

Cada porta possui

- PCB própria
- LEDs RGB
- Pogo Pins
- Conector para placa principal
- Proteção ESD

Distribuição

Uniformemente ao redor do poliedro.

---

# Áudio

Amplificador

MAX98357A

Interface

I²S

Alto-falante

4Ω

1~3W

---

# Vibração

Driver

DRV2605L

Tipo

ERM

Controle

I²C

---

# RTC

Modelo

DS3231M

Interface

I²C

---

# USB

Tipo

USB-C

Funções

- Programação
- Alimentação
- Atualização
- Comunicação

---

# Organização do Projeto KiCad

```
DK01/

    Documentation/

    KiCad/

        MainBoard/

        DisplayBoard/

        DoorBoard/

    Firmware/

    Mechanical/

    Production/

    BOM/

    STEP/

    Images/

    Datasheets/
```

---

# Organização do Esquemático

01_ESP32

02_POWER

03_USB

04_BATTERY

05_DISPLAY

06_AUDIO

07_HAPTIC

08_RTC

09_FLASH

10_PORTS

11_DEBUG

12_CONNECTORS

---

# Organização da PCB

Main Board

Display Board

Door Board

---

# Objetivos da Fase 1

✔ Definir arquitetura

✔ Escolher componentes principais

✔ Definir organização do projeto

✔ Definir barramentos

✔ Definir formato mecânico

✔ Congelar requisitos

---

# Critérios para Encerramento da Fase 1

A Fase 1 será considerada concluída quando:

- Todos os componentes principais estiverem definidos.
- Toda a arquitetura elétrica estiver aprovada.
- Toda a arquitetura mecânica estiver aprovada.
- Toda a estrutura do projeto KiCad estiver definida.
- Não houver dúvidas abertas que impeçam o início do esquemático.

---

# Próxima Fase

## Fase 2

Desenvolvimento do esquemático completo da placa principal no KiCad 10.0.4.

Será definido:

- Todos os componentes
- Todos os valores
- Todos os footprints
- Todas as conexões
- Regras de projeto (ERC/DRC)
- Preparação para layout
