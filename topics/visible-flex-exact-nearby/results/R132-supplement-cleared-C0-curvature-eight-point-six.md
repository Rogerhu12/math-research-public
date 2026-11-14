# R132 续篇：完整清分母残差给零阶误差 .000834 与曲率 8.552

2026-11-13。

**已执行并通过。** 对同一原始固定目标、同一腰初值以及完整
η∈[−10⁻⁹,10⁻⁹]，全部150个闭盒的清分母残差与独立R131最大值
屏障给出真实[-.05,.05]分支的误差小于.000833048、实际Riemann
间隙大于.24351896436，主曲率绝对值小于8.551947。
本篇保留同一输入上R134能量门的实际失败；没有将失败改成成功，
也没有将局部几何量称为最终闭面的reach。

## 1. 同一实际对象与完整残差

固定δ*=−7789843107295549/4611686018427387904，原目标
E(r)仍是初始候选完整|F_r|²的角平均。不同辅助δ不被称为同度量flex。
有限比较对象是原75片、512角模式存储的完整degree7候选；每片再分2盒，
共150盒。每个盒留在一个真正common scalar germ，所有准确端点、mean、
整个参数盒与原无限primitive余项均保留。

[R134清分母证明](R134-supplement-complete-cleared-polynomial-residual.md)
给出先形成完整NB=C²RB与NC=CRC，再取全角闭单元界、最后除以负C
的准确程序。角乘积degree≤765，2048无alias网和4096个闭角单元覆盖
所有乘积与角圆；真K、γ、β二阶余项没有删除。

完整原生运行1541.766秒结束，150行、failure=null，准确区间[0,1/20]。
此producer仍明确continuation_certified=false；存在性来自下一独立消费者。
若实际germ约10⁻¹⁶长，有限dense多项式的径向微分会产生很大的保守点值界。
所有这些盒均实际保留，屏障使用其准确长度；没有合并接缝、删行或以
平均残差代替整盒上界。

## 2. 真正通过的R131最大值屏障

消费者逐项核原producer、所有原生输入/依赖SHA、原腰对象、中心参数、
η盒和完整角域。真实初始加权角梯度由已认证的原腰独立输入，
不是候选的导数误差。它只把数学上同名的边界量交给冻结的R131 v2
传播核；原报告kind/source不被改写。

对每盒完整使用
\[
D^+e_0\le A_0e_0+\rho_0,\qquad
A_0=\gamma D_1+|\beta|(1+3M_b^2)+2|\kappa|,
\quad M_b=\widehat M+1/16.
\]
严格仿射屏障、真实gap与连续性bootstrap全过，得到
\[
 e_0(1/20)<.000833047006630<.000833048,
 \qquad\inf(q-p)>.24351896436.
\tag{C.1}
\]
初始误差屏障小于4.214784×10⁻¹⁰；真实加权角梯度由221.387251
传播到小于256.843003，真实一阶角导数全区间小于1042.330379。
后一个数只是充分有限性界，不是C¹误差或候选的精度声明。
R131的线性退化结构因此闭合真实C¹延拓；不是一个假设解已存在的条件估计。

## 3. 同一输入上的能量门确实失败

另独立运行原R134两个线性能量屏障和含mean Sobolev恢复门，固定同一
1/16管。它通过前44盒，在零基row44（第45盒）失败：
\[
[8147697855416153/576460752303423488,
 16787232508075617/1152921504606846976].
\]
该盒恢复的C0界为.0638827350086>1/16；此前通过部分的最大界为
.0610419431127。完整failure字段、全部已算行与真正通过的前缀均保存。
它不否定R134定理，也不否定实际解；它表明这组保守常数下该误差门
不足。最大值门与能量门是两个独立充分条件，本篇只以实际通过者认证全段。

## 4. 新的实际曲率与水平框架结果

R132不变矩形已从同一腰和同一目标证明p<0<q及唯一性，故其符号
可与(C.1)的同一分支比较。对每盒真实M和gap g使用准确估计
\[
0<A\le kM,\qquad |B|\le k,\qquad |C|\le2k/g,
\]
\[
\max|\lambda_j|\le\max\{kM,2k/g\}+k.
\tag{C.2}
\]
这给整个[-.05,.05]、全部η的
\[
\boxed{\max|\lambda_j|<8.551946246853<8.551947.}
\]

水平框架沿用已证明的完整积分估计，所有源与初始方向都不变：
Xh(0)=0、Xturn=∫√E|A|、Yturn=∫√E|B|，
Δh≤∫√E min(1,Xturn)，Nh≤Yturn+Xturn²/2。
初始支撑>1/2、半径<13/10，得到下表。

| 全区间量 | 安全有向界 |
|---|---:|
| 水平位置位移 | <.003969888481 |
| Xturn | <.142347612195 |
| Yturn | <.051661238604 |
| 水平法向变化 | <.061792659952 |
| 水平半径下界 | >.496030111519 |
| 角分子det_h(Fh,Yh) | >.428870501335 |
| 水平法向支撑Fh·nh | >.415699653581 |
| φθ | >.269562903830 |
| 柱Jacobian | >.289672670215 |

新曲率更紧；较粗150盒对E等系数的覆盖使本表某些水平量略弱于原300盒，
不宣称每个常数都改善。两证书都属于同一分支，各自界仍有效。
完整几何consumer验证150行逐一对应、所有门、同一原腰和真实符号证书。
正φθ与柱Jacobian沿R132的固定φ高度单调论证给同一精确嵌入。
没有把.05曲率界移植到已证.07环带的外层。

## 5. 固定输入、源码与复现

下列源和原生输出全部保存；其余原对象/candidate依赖由native逐项绑定。

- `scripts/fourfold_codazzi_cleared_polynomial_residual.py`：`ae4711afa7df6106138fe63842a8f983f41a249209d2c60ad74ed5326da375d3`。
- `scripts/fourfold_codazzi_cleared_C0_continuation.py`：`f4113fd2a03b747628fdfa601c972e9847fb8ecb13156e8b400b331224e3b535`。
- `scripts/fourfold_codazzi_weighted_error_barrier.py`：`b2eeb60d639cc5af662f81a963def514f7fc4093a2c4bb806cc34fe1a7eebd6b`。
- `scripts/fourfold_codazzi_cleared_C0_geometry.py`：`abea60933683cf920348317e8580b88d4c966803f142650d8a317893a50c9003`。
- `notes/2026-11-13-Codazzi-cleared-polynomial-r05-v1-native.json.gz`：`7c72d58bac382aabd78bf981b81072c663b1a9bde0f86705d4fbb796bd44d051`。
- `notes/2026-11-13-R131-cleared-full-r05-v1-C0-native.json.gz`：`2fbd72039e418310ddb42bb2a22ca2e7afced5a5a470d9f26ac0d366f10ec4c3`。
- `notes/2026-11-13-R134-cleared-full-r05-v1-energy-native.json.gz`：`f1c9fa556a691a56b7f91f5344dbf164da7153e9bfa18a5f7992d344bdfb38ca`。
- `notes/2026-11-13-R132-cleared-C0-geometry-r05-v1-native.json.gz`：`d11652b453fdcbc5e79bffc12dc36441b033364b1b83bce726990cfb58db1a7d`。

三个消费者分别可在新的输出路径重跑：
```bash
python scripts/fourfold_codazzi_cleared_C0_continuation.py \
  --native notes/2026-11-13-Codazzi-cleared-polynomial-r05-v1-native.json.gz \
  --out /tmp/cleared-C0-r05.json.gz
python scripts/fourfold_codazzi_weighted_error_barrier.py \
  --input notes/2026-11-13-Codazzi-cleared-polynomial-r05-v1-native.json.gz \
  --out /tmp/cleared-energy-r05.json.gz
python scripts/fourfold_codazzi_cleared_C0_geometry.py \
  --out /tmp/cleared-geometry-r05.json.gz
```
使用HANDOFF规定的python-deps、单线程环境；消费者必须给新输出路径，
不得覆盖原报告。本结果只改善同一局部真实分支。更远区间、跨根/正帽、
全尾regular/mean与最后公共度量族的所有几何条件继续是实际缺口。
