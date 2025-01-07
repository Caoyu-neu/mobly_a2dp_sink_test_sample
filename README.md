# Welcome to Mobly

[![Latest release](https://img.shields.io/github/release/google/mobly.svg)](https://github.com/google/mobly/releases/latest)
[![Build Status](https://github.com/google/mobly/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/google/mobly/actions)

**Mobly** is a Python-based test framework that specializes in supporting test
cases that require multiple devices, complex environments, or custom hardware
setups.

Here are some example use cases:
*   P2P data transfer between two devices
*   Conference calls across three phones
*   Wearable device interacting with a phone
*   Internet-Of-Things devices interacting with each other
*   Testing RF characteristics of devices with special equipment
*   Testing LTE network by controlling phones, base stations, and eNBs

Mobly can support many different types of devices and equipment, and it's easy
to plug your own device or custom equipment/service into Mobly.

Mobly comes with a set of libs to control common devices like Android devices.

While developed by Googlers, Mobly is not an official Google product.

## Compatibility

Mobly requires *python 3.11* or newer.

Mobly tests could run on the following platforms:
  - Ubuntu 14.04+
  - MacOS 10.6+
  - Windows 7+

## System dependencies
  - adb (1.0.40+ recommended)
  - python3.11+

## Installation
You can install the released package from pip

```sh
pip install mobly
```

or install from the source to use the bleeding edge:

```sh
git clone https://github.com/google/mobly.git
cd mobly
pip install -e .
```

You may need `sudo` for the above commands if your system has certain permission
restrictions.

## Tutorials

* [Mobly 101](docs/tutorial.md) -
Simple test examples to get you started with Mobly.

* [Mobly Instrumentation Runner Tutorial](docs/instrumentation_tutorial.md) -
How to use Mobly's Android instrumentation test runner to run Android instrumentation tests.

* [Mobly AndroidDevice Service](docs/android_device_service.md) -
Create custom service to attach to Mobly's `AndroidDevice` controller.

## Mobly Snippet
The Mobly Snippet projects let users better control Android devices.

* [Mobly Snippet Lib](https://github.com/google/mobly-snippet-lib): used for
triggering custom device-side code from host-side Mobly tests. You could use existing
Android libraries like UI Automator and Espresso.
* [Mobly Bundled Snippets](https://github.com/google/mobly-bundled-snippets): a set
of Snippets to allow Mobly tests to control Android devices by exposing a simplified
version of the public Android API suitable for testing.


## 关于mobly_a2dp_sink_test_sample
基于google mobly master fork出来的分支，追加了测试case样例，用于测试esp32 bluetooth sink和树莓派source之间蓝牙音频通信（classical，A2DP pipeline）。

测试样例位于a2dp_sink_test_sample文件夹下。

测试命令为：
python a2dp_sink_test.py -c sample_config.yml

测试环境配置方式参照a2dp_sink_test_sample/测试环境说明.xlsx中。
