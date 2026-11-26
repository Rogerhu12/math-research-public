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

## v2 的真实准备返回

同公开 run45811843606/1 的真实 stage6 已在 312.14789570699986 秒完成，exit0，无缺 outputs 或 summary errors。执行 checkout `220a65acdced5353a16faac6ff7ac52d0aba2a8b`，完整 provider `4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3`；队列源提交为 `67020b5a9326ec17ce759aa4c8d16bb54e917498`。原失败没有删除。完整实录与全部实际 argv 保于[实际第1卷](2026-11-26-public-actions-45811843606-1-part-001.md)。

|实际输出|字节|SHA256|
|---|---:|---|
|report.json|29803|`b3a0fe75d3d97c42e9faa32fb70f6ec8625e39c7aea6a90831bc72bf0c4f6de3`|
|reference.npz|866178|`3cb4a0ad8bb126a71c1f088e240a70fb7ae3852f7720837f5fb5bd2278efe2f0`|
|observations.npz|227217|`8a0dd540a98c51dc5dcba1ccba8ca942cdda122e5c9a37a7b73e353e14c4b55c`|
|locations.json|106450|`73ea6cd6eee84f8940b4b9657b5bc50986242e3ece86d70b7c6dd6070c6e6926`|
|supplied-location-provenance.json|223619|`b51791038ce011571f7b6a17701c8b3095af8ceccbc126cf3397899be6d55704`|

这次实际固定 profile 是 `e3a06cbe5799b16a50544f34bd91f876017cdfd22e2f56fc0ba69fd9b05bb00b`，model 是 `4cdb25528b9275438bd5acc78b08440bea4609240547dc92f42b7b11a2b40772`，原 scalar 参数 identity 是 `e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa`；没有预填旧383168或另一个run的identity。

实际 M160/J923/N2048/P7377 全保；新自由H的工作种子为1.9470544370684175，准确定义仍是自由H，未把工作积分当精确积分。标量无限尾盒有效、1512 leaves，300秒请求精度仍为false；R载体误差2.373129134780865e-13。14753次完整T0查询的四标量读数误差分别为5.41898353418071e-14、5.413532044282941e-14、1.4980181584957043e-12、9.453185076344921e-11；这些不是完整场、trig/归一化、Gram或连续几何证书。

全部已提供11历史payload转换后实际1250个curvature、208个radius地址、18个protected curvature、1782个记录occurrences，pending grid为0；保literal binary位置、未round或虚构其它runner后继点。输出只留runner，公开上述身份和紧凑读数。此时物理F/Gram尚未读、新方向尚未返回；后继完整hDelta与零Delta实际求解继续。
