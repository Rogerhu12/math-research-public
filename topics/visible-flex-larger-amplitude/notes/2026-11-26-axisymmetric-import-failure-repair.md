# 独立 axis 入口的实际导入故障与最小修订

公开 run45811843606/1 的 stage2 使用 e3fb126b 准备源，5.938221273 秒返回1，五个声明输出都未产生。stage3/4 仅因缺父文件在setup阶段失败，未执行科学方向。根的纯日志读取随后确认实际异常：e3fb paths_and_modules 调用 hold role，ed6 原 IVP 第13行的同目录裸导入 parallel_20261117_profile 在 resume_20261126 入口下找不到。实际完整log1763B，SHA256 2387b14d1ed65c75be688e2fbf93c7bbbca2122984a28a36649ce6e0b8f6b6c1。

修订只让 observed/scalar/deep_scalar/history 四个实际消费模块执行导入。warm_producer/integer/hold 三个来源仍逐字核路径和SHA；原 FullHold 继续自行加载准确 integer oracle，并核 hold 文件身份。没有增加sys.path或伪造模块，没有松动真实输入守卫，也没有改变标量、T0、场、J/J*、母范数、QP、幅度或永久位置算法。

prepare之外五后继只更新闭合来源常量。实际AST比较确认 provider仅paths_and_modules改变；其它五源的全部科学声明与函数相同。六源实际AST/compile及尾空白检查通过。无本地F/J或fixture。正常新提交保留ace40095的完整失败源码快照；新三步明确用v2新ID与新输出目录，旧失败不覆盖。summary沿根已修的scalar-only selectors。

此修订不预报科学运行成功；下一次完整真实准备将继续支付全部原定输入和缓存，随后才有首完整新场方向。

## 完整来源与真实归因绑定

旧六源完整快照保留于普通提交 `ace40095a2b343629a4adaa9cd73d34ac098b0a4`；新源逐字刊于原路径，科学函数未改。新三步完整参数见 `computations/resume-20261126-axisymmetric-so3-v2-first-steps.json`。

|完整文件|字节|SHA256|
|---|---:|---|
|`fullclosed_axisymmetric_so3_qp.py`|46828|`606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9`|
|`launch_axisymmetric_so3_actions.py`|9430|`a94263f037dfa8535b11cf44fa93b6a4cd6df7dee1a6be35f2ea14f5abaa2690`|
|`read_axisymmetric_so3_report.py`|16133|`6d54cbba7ff998bc98b0f39c6a26ae33c16957fb0b9dc0fffced1037212455eb`|
|`so3_axisymmetric_meridian_geometry.py`|43931|`2240a1f68021991a85c502ed3cf67c82f6bac6e1e4e10b3b3286eab120d4f229`|
|`so3_axisymmetric_meridian_operator.py`|38974|`7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf`|
|`so3_axisymmetric_reference.py`|46198|`4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3`|

真实 stage5 用纯归因源 `ef017af52fd8b9801434b3af655f9fccb7d7a51e9bf0abb3ff5e85496659e338` 读取本 runner 已有 stage2 traceback，6 秒内返回（实际 5.906384144999947 秒，exit0，无缺项）。紧凑归因 JSON 2989B / SHA256 `6d862dc099a9be0191878cd5e9cd919f9f5bbea40bd5c6f0465e3634dc8efb21`。这不是新场、方向或连续认证；完整原日志留 runner，公开只记确认异常与身份。
