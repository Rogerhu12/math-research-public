# R815：原 Wronskian 乘法矩阵 Mg 的准确有理重构已完成

日期：2026-11-16 UTC。会话：serre-public-astra-20261115。状态：原 $M_g$ 的完整有理多项式矩阵及齐次第二图已实际认证；同一生产任务的 $\Gamma$ 仍未完成，整任务的 complete=false 保留。

## 1. 实际完成对象与运行

本结论来自公开 [run43809724947](https://github.com/Rogerhu12/math-research-public/actions/runs/43809724947)，job133108436809，source commit
8adc90dfe2c6943ab3ba3eaf67a52682302026a3。

读取的实际完成索引为
R815-target-g-component-00-certified-multiplier-index.json.gz，
7469 bytes，SHA256
f27130f00ea3b2cd17284e531eb8f6145b37200c49e7002baf0b7cd053281033。

它记录原目标 g、field_component=0、coefficient_field_basis 为
“Q in the unchanged original K-normal basis”，以及：

- 原首列已逐系数准确认证；
- 完整多项式交换子恒等式已认证；
- 所有逐项加权次数界已保留；
- 原 cyclic 唯一性识别真正的正规乘法矩阵；
- 齐次第二图保同一个原截面；
- 所有原标量和系数域规范保持；
- 没有形成特征零 Krylov 矩阵的逆。

实际重构使用696个原顺序素数，最后一个为1000014397，CRT 模数 bit 长20809。原完整素数顺序留在该完成索引中。这个计数只描述实际重构输入；准确性来自下文的有理恒等式及唯一性，不能仅由 CRT 模数大小推出。

## 2. 原对象、基与尺度

沿 [R813 的完整证明](R813-original-Wronskian-normal-derivation-and-cyclic-certificate.md) 和
[R815 执行契约](../notes/R815-original-normal-derivation-operator-method.md)，保原曲线 $Y/K$、$K=\mathbb Q(\zeta)$、原 level82 与原正规基。

原铅笔为
$$
\tau=e_0,\qquad \sigma=e_1+n e_{73},\qquad z=\sigma/\tau,
$$
其中实际原 n=1，由原源读取。原次数为
$$
\epsilon=(0,1^{144},2^{127}),\qquad
\beta_a=d_a/\tau^{\epsilon_a},\qquad\beta_0=1.
$$

原 Tate 微分尺度、原导子及输入函数仍是
$$
D_0=\frac{q_Y}{82}\frac{d}{dq_Y},\qquad
\delta=\tau^{-1}D_0,\qquad
G=\tau D_0\sigma-\sigma D_0\tau,\qquad
g=\delta z=\frac G{\tau^3}.
\tag{815G.1}
$$

原 R813 第0列 S3 坐标给准确正常向量 $v_g$。程序读取完整的 coordinate numerators、column denominator 和原 rational scale，只施尺度一次。实际目标配置保
original_rational_scale=[6724,1] 和
original_D0_qY_multiplier=[1,82]；这两个字段必须按原 R813 的准确坐标合同理解，不可另补一个 $82^2$ 或去除 content。

原 R813 两列准确 S3 坐标为950296 bytes，SHA256
29bedd339da16b4fee3dfd412f1d599343a25231fa3b360f5b7b6be4404e9085；
normal interface 为8761 bytes，SHA256
ef9d09186098bd8cc2144c16bf7797234ac176b7d1faac3fd50b74564c6f32a6。
这两个 Wronskian 输入及原820行认证没有重算。

本结论说固定原 K-normal 基中的矩阵系数属于 $\mathbb Q$；不把原 K 曲线或每个原截面另宣称为 $\mathbb Q$ 定义。

## 3. 完整多项式矩阵的准确认证

以输出行 b、输入列 a 为矩阵方向，真实乘法矩阵满足
$$
M_g\in\operatorname{Mat}_{272}(\mathbb Q[z]),\qquad
\deg(M_g)_{ba}\le3+\epsilon_a-\epsilon_b\le5.
\tag{815G.2}
$$
负上界表示对应条目必须为零。

重构所得候选记作 C。候选按17个块保存，每块16个输出行；每块保共同正分母，以及按“输出行、输入列、幂次升序”排列的整数分子。重构采用原严格有理重构范围，完整的加权支撑检查保留全部零约束。

首先，程序逐幂次、逐输出坐标准确清分母检查
$$
Ce_0=v_g.
\tag{815G.3}
$$
相应证书为
R815-target-g-component-00-attempt-000696-exact-first-column.json.gz，
2351 bytes，SHA256
e2ee6e2829d52cb5411a53363c8fcd03e989127f4c34329952f7f8a7d6aa72ae。

令 $W=M_w$ 为已成原 primitive 乘法矩阵。它仍来自 R806 的准确完整多项式输入，SHA256
63b38d14dbeb4b504619db65f56c151146885173b8cef253dfba3bebc76cd2dd。
加权乘法给
$$
\deg(CW-WC)_{ba}
\le4+\epsilon_a-\epsilon_b\le6.
\tag{815G.4}
$$

本次实际在全部七个不同整数点
$$
z=0,1,2,3,4,5,6
$$
逐272×272完整矩阵检查 $CW-WC=0$。每个点均按17个原行块，在清除真实正分母后计算两个整数矩阵乘积，核每个整数残差为零。没有用随机模点或一条首行替代全部方程。这些终验点无需是 Krylov 好点。

次数至多6的每个有理多项式有七个准确零，故
$$
CW=WC
\quad\text{在 }\mathbb Q[z]\text{ 中恒等成立}.
\tag{815G.5}
$$

原 R806 cyclic 见证仍为374731 bytes，SHA256
6d6722d93321e757535fe96f9d3ecc181ac85dc65d67d4bda41a6477ab84f5e8。
它证明 $e_0,We_0,\ldots,W^{271}e_0$ 在 $K(z)$ 上为基。真实几何乘法矩阵 $M_g$ 与 W 交换且有首列 $v_g$，于是
$$
(C-M_g)W^je_0
=W^j(C-M_g)e_0=0,\qquad0\le j\le271.
$$
因此 C 正是原 $M_g$。这是完整特征零认证；它不依赖猜测未知系数的最终大小。

七个准确点索引以及各自全部行块、完整候选和34个两图矩阵块的身份，均由7469字节的已成索引完整绑定。新的消费者直接读取这些已成块，不再次进行696个素数的重构。

## 4. 齐次第二图与同函数运输的区别

令 $t=1/z$，并令
$$
D(t)=\operatorname{diag}(t^{-\epsilon_a}).
$$
本次另外保存原截面 G 的正规第二图乘法矩阵
$$
M_{G/\sigma^3}(t)
=t^3D(t)M_g(1/t)D(t)^{-1}.
\tag{815G.6}
$$
每个加权条目按其准确上界反转系数，保原正分母；程序逐项确认指数非负，并逐系数检查运输后的原首列。

如果消费者需要同一个有理函数 $g=G/\tau^3$ 的第二图矩阵，则应使用
$$
M_g^\sigma(t)=D(t)M_g(1/t)D(t)^{-1}
=t^{-3}M_{G/\sigma^3}(t).
\tag{815G.7}
$$
不能把(815G.6)直接称为同函数 g 的矩阵，也不能因此丢掉真实的 Laurent 因子。与 $\Gamma$ 的第二图配合时，仍须保 R813/R814 的导子变换和底变量微分负号。

本次第二图是原截面乘法的准确运输；尚未声称完成 $\Gamma_\sigma$。

## 5. 实际源、索引和续接身份

| 项目 | bytes | SHA256 |
|---|---:|---|
| 原 g 正常向量 | 286121 | add3163f9313522bc930c91ea3cbc961d7e09009bd2c58941e15400a1caf9c71 |
| 第696次完整候选索引 | 8606 | 28d3bf763174e43a5c78f190887460e52d920c8fdaa9917a27334633eaffee76 |
| 第696次 CRT 小历史 | 3907 | 9195c6b23974a0995cb5a98d69b98478c13aa13fa0f91606cba6481165492d6d |
| g 完成索引 | 7469 | f27130f00ea3b2cd17284e531eb8f6145b37200c49e7002baf0b7cd053281033 |
| 完整输出 manifest，6718项 | 1737821 | 18b1f497da468e22f016341cf140cc5e5b58917c49b3b11701a063ef4b08dd06 |

目标配置 SHA256 为
88c00c7f1d65fb8ae4f2350ee26fa4f6b8d2cd73612b15ca7d3d183fc7720ca6；
共享原正常基配置 SHA256 为
b92034874a9afe85d74112e8b429de1f0be67ef10dc4fabc7c5d92c741e64cec。

冻结 core、wrapper 和 R811 framework 的 SHA256 分别为：

- 80516ff9598fdb6251628c00794dc3529b998a7c563fe80fd9c31406e3896c7d；
- ab725da038ec458493f461088ceee0fd105e0dc90cbfb4ad6f3047cbec90b454；
- 849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3。

完整原输出 artifact14216992068，
serre-global-R815-original-normal-derivation-operators-43809724947-1，
4686023089 bytes，平台 ZIP SHA256
190f59de642538073aa61ae9e5e8d1488fd035741eadc4d17de92e391171d429，
到期2026-11-17 10:27:27 UTC。

必要回读由公开纯 IO run43853409641 和
run43853961723/job133253479810 完成。后一个 g-index 回读只抽所需小件，实际1279259 Range字节、12次请求；选取包367856 bytes，SHA256
2988995a0d2407dc0d27bbca85b23e49686fa7827ef78668478f60cea4ecc482。
它按原完整 manifest 核所选成员，没有另声称重哈希整个4.686GB ZIP。

## 6. 真实停止原因与后继未完成项

原运行在2026-11-16 10:27:23 UTC结束，core 实际抛出
BudgetStop: Complete original operator stages and latest CRT states retained.
实际 traceback 已进入 $\Gamma$ 的新 modular image，不能将整体 failure 解释为 g 的准确认证失败。核心完成标志仍为 false，wrapper 的 process_exit_code 为1；全部完成原子阶段和当前 CRT 保留。

新的同核续算
[run43853995004](https://github.com/Rogerhu12/math-research-public/actions/runs/43853995004)，
job133253466821，source
c1b3bfb1a0deae3c4b75da514ffcbb8530ae59d3，
只更新至该实际输出 artifact 并继续300分钟。已成 g-index 会直接返回并沿原引用验证完整已成阶段；它不重新作 g 的 CRT。后续继续原 $\Gamma$，保同一 $M_g$、原 h 向量及七点嵌套交换子认证，不独立重构 $M_h$。

此次关闭的接口是原 $M_g$ 的准确有理重构和齐次第二图。原完整 $\Gamma$、两图连接、极理想、原五函数的后继 RR、Hecke 支持、全部非 p 项、周期和高度，仍按各自任务继续。已经完成的 R827 固定辅助素点导数算子仍可供既有模消费者直接使用，无需改用或重算本次大有理矩阵。

所有新数学均在本公开仓库 Actions。矩阵、向量和机器证书只在当前必要的一日产物内续传，Git保存本证明、程序、参数与实际身份。
