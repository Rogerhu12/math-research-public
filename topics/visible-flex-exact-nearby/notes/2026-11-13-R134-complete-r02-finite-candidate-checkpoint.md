# R134 检查点：到 r=1/5 的两个完整有限候选与无损存储

2026-11-13。**有限候选完整保存；PDE精度和延拓尚未由本记录认证。**

两个运行都保持原固定目标、同一腰初值、同一δ中心，并在每一个实际
common scalar knot重启DOP853。每段存储完整degree7多项式的共享端点
和六个dense correction；每个binary64实/虚部按准确dyadic解释，
负频率是正频率的准确共轭，mean保留，Nyquist准确为0。
所有角导数在共享端点连续；不声称径向导数在接缝连续。

| 项目 | 512角点候选 | 1024角点候选 |
|---|---:|---:|
| 正频率数量（含mean） | 256 | 512 |
| 完整径向片数 | 284 | 283 |
| 实际scalar stages | 141 | 141 |
| 原gzip字节数 | 15,738,642 | 31,107,692 |
| 保存分片数量 | 4 | 8 |
| producer耗时 | 182.203秒 | 120.318秒 |
| 采样Riemann残差C0 | .00302621784 | 3.91641160e−7 |
| 采样Riemann残差角一阶 | 3.29685075 | .000829361021 |

采样表只在原producer的21个径向点与有限角网读取，不是全盒、全角、
全η或舍入误差证书。径向中间值可能更差；有限ODE收敛也不等于原PDE。
后一候选改善了这些采样量，因而用于新的实际连续清分母验证。

## 1. 完整对象的准确身份

- 512原gzip SHA：`3c0a07ca5ea76046d4248452d429677b6e9faa5bbada175d41ac8f7faec85e58`。
- 1024原gzip SHA：`da1dcc9e5dbeff97998023db376c9e0c3fcfae48639cc1639dba57c7494c91a3`。
- 共同producer：`scripts/fourfold_phase_codazzi_dense_candidate.py`，SHA
  `81630e41d5fb8d34f9424d291a35000371a15e21778dbbb19e0272f2edc151c2`。
- 原对象：`data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json`，
  SHA `91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848`。

候选准确的最后dyadic端点略大于1/5，故请求的准确1/5位于完整最后一片中。
全部准确时间、原germ元数据、端点数组和6个correction数组保留，
不是从少量采样点重新插值，也没有只保存低模式或只保存端点。

## 2. 无损字节分片，不改变数学对象

`fourfold_codazzi_sharded_candidate.py`将原完整npz.gz的连续字节按至多4MiB
分片，每片再独立gzip。它保存每片的准确offset、原字节数、payload SHA、
存储SHA和完整原gzip SHA。解开外层gzip并按offset拼接，逐字节恢复原gzip；
再按原方式读npz便得到同一完整数组。

每片存储小于5,000,000字节。此分片只是遵守单件大小限制，未删改任何
Fourier系数、径向端点、mean、浮点二进制字节或producer身份。
`ShardedExactCandidate`在验证全数组后直接继承冻结ExactCandidate的
同一个polynomials函数；`ShardedDenseCandidate`同样继承原evaluate。
root已对两个完整原gzip验证逐字节等同、全部数组/分片/metadata相同和
上述继承函数身份。读取时再次逐项SHA校验；缺片、错序、错offset或
任何完整SHA不符都会失败。

完整分片清单由下列两个manifest准确列出；它们是可重建的原始数据，
不是仅记录“文件曾在scratch中”的收据。

- `notes/2026-11-13-codazzi-dense-r02-n512-candidate-shards.json`：`809d5a3d896ee4b5344a8c58b7fb5814ae5cb06c735fd8b7ba9aa962a4d04ccc`。

- `notes/2026-11-13-codazzi-dense-r02-n1024-candidate-shards.json`：`715b139505c8b7a34ca06e0cbadbd109e777205ede11f6cf7a2f753861fa1316`。

存储/读取源码SHA：`ecefafa9a47495b050332893a0acd9fb3f3143c0c1b59d2e99c01813bdc25b92`。


## 3. 复现与下一实际消费者

原候选的运行参数为`--right 1/5 --angles 512`或`1024 --max-step .001`，
rtol=3e−11、atol=3e−13、primitive_nodes=512、nonlinear_grid=2*angles。
要消费已保存的准确对象，可直接把相应manifest交给ShardedExactCandidate，
无须再次依赖浮点ODE能否逐bit复现相同轨迹。

新完整清分母验证另立producer/source/native身份，并支付原真实目标的
高阶导数、原无限primitive、全η、整个闭角圆与每个真实径向germ。
只有随后真正通过的延拓门才能扩大已证明的精确分支区间。
