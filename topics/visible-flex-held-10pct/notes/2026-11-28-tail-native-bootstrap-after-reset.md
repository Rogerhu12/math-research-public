# scratch 重置后的原 native bootstrap 实际恢复

状态：**必要输入/执行器恢复，真执行完成；不是新的数学结论。**
原 70 源、shared-source/modules、port/chart 由 design 唯一恢复。
本条仅复制这些真实静态源并恢复原 periodic/chord/native bootstrap；
没有求旧 q=.06、旧 full-H、旧 1152 段几何或 R90 证书。

## 真执行

原生产 C++ 源
`scripts/resume_n4_tail/native_extended/frozen_flow_production.cpp`
SHA `e5a7d3b0a1021aae54fabcd3c5baae0558cab4246b4a10cfdeb31b6d275a8ddf`，
header SHA `88d7b9bc6c92a3d73ca33b2152e8bac078b6c9b3f90167f5e0a3409dd01f8356`。

实际使用 Debian g++ 14.2.0：

```text
g++ -std=c++17 -O2 -fno-fast-math -ffp-contract=off
    -fexcess-precision=standard -frounding-math -DVF_BUILD_MAIN
    <repo>/topics/visible-flex-held-10pct/scripts/resume_n4_tail/native_extended/frozen_flow_production.cpp
    -o <work>/frozen_flow_batch -lm
```

这是原 `tail_recovery_setup.py` 的完整编译选项。
TTY4091 实际 return0，墙钟 3.431765622 s；
生成 125248-byte executable，
SHA `1b47ed47e70e35a08f11173b1f17a5d1c2ee046f59f54f235ee5fa56de07af94`。
只称本环境原源码/原flags的真实新二进制，不声称恢复旧二进制字节。

从实际 shared-source 复制 periodic-source 后，
原 `install_periodic_quadrature.py`、
`install_bounded_chord_tail.py`、
`prepare_recovered_native.py`
顺序真 return0。完整实际 argv、日志/manifest SHA 与状态见配套小 JSON。
bootstrap scope 精确是 M24/spacing3/quadrature512/steps16/workers2，
和原 bootstrap 相同；不把这当最终高 M 场的运行 scope。
新 QR/original7a coordinator 会在真正 λ1 到来后按其完整实际 M/N/config 另建 native4。

实际生成：

| 输入或输出 | SHA-256 |
|---|---|
| `inputs/reference/chart.json` | `dc85dda524e03896b4afa552bd1f859b73cf96f88033565ff910e227034f2f93` |
| `m24-tail-settings.json` | `37bc9073d2dba1d110b165b5febbb054d1dd1a8ca09ec23b86e2d76c39f08f46` |
| `m24-linear-port.json` | `42369d1571413fd4ecccea43ccfef233f4b97506f71e28b86ed9735c28c2d93b` |
| `native-tail24/native-manifest.json` | `c1ddc4fee28a7d5c157a771a1276a0c57def8ab9483936725482ab191cfaed53` |
| `recovery-setup.json` | `3f5302c7186e823e16ac934824e3d507bfd56fa75958b980239573cdbcf0e8d8` |

上述路径都在
`/workspace/scratch/7c4e33ee17de/held10-design-work`；
数据/二进制不入 Git。

## 来源与预检

新的 recovery-setup 明确记录：
原 all-in-one `tail_recovery_setup.py` **没有**整条重跑；
前半输入来自 design 真完成的
`R87-input-recovery-after-volume-reset.json`
（SHA `49ff67e14179c31b2c0e3ceb067c131163e4e79e4f7cd819f7ce5fbec86fc4c2`），
后半来自本次实际编译与原 installer。
因此新文件是诚实的新执行来源合同，非伪造旧 setup 终态。

原 QR coordinator 的 `verify_references(native_manifest)`
已实际逐条核通过；
原 `equal_prefix_python(multistage-source,chord-source)` 也实际通过。
小报告
`native-recovery-build-20261128/bootstrap-verification.json`
SHA `adbed7eefee578795d741fb48b2b3bfd00ba4b036a27bedb056663a4d18af9e0`。

它只核可执行器/原数学源码与完整输入身份；
没有启动 native flow、shooting、BVP 或 positive λ1/source gate，
没有把编译成功等同于完整新场验收。
