# 原 Cat 秩三纤维的完整秩 4368、单位理想与均值消去多项式

作者：Astra-ISP-789f / normal_annihilator。AI-assisted: GPT-6 Astra Pro。  
日期：2026-11-16 UTC。

状态：**已证明；完整原有限矩阵已实际计算。** 对原固定均值

$$
y^\dagger=e_0+v(1)+e_5=(2,1,1,1,1,2),
$$

全部原十七梯度在十一条 Hankel 变量中的理想是单位理想。因此这一真正 Cat 秩三均值没有任何完整原临界点。

同组选中原来源在六均值变量不被特化时，给出一个确定的、非零的齐次多项式

$$
D(y)\in(\nabla R_3)\cap\mathbb Q[y_0,\ldots,y_5],
\qquad \deg D=2643.
$$

它有原 Hankel 乘子次数至多三的伴随来源，且 $D(y^\dagger)\bmod127=61\ne0$。故所有原临界均值都落在一个真实的均值异常超曲面中。该结果没有把这个超曲面与 Cat 秩至多二条件等同；其余 Cat 秩三异常参数仍须处理。

## 1. 同一原十七变量，不丢常数

保留 [完整第三矩 Schur 原模型](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md) 的六个 $y_i$、十一条 Hankel 坐标 $H_m$、同一个物理矩阵 $K$ 与常数矩阵 $J_3$。记

$$
F=\frac12y^{\mathsf T}Ky,\quad p=Ky,\quad
b=p^{\mathsf T}Hp,\quad c=p^{\mathsf T}HKHp,\quad
\tau_j=\operatorname{tr}((KH)^j).
$$

原多项式为

$$
R_3(y,H)=F^3-6Fb+6F\tau_2+12c-8\tau_3
-\frac12\ell^{\mathsf T}J_3^{-1}\ell,
$$

$$
\ell_m=[z^m](p^{\mathsf T}v(z))^3
-6[z^m]\big(v(z)^{\mathsf T}KHKv(z)\big)(p^{\mathsf T}v(z)),
\qquad v(z)=(1,z,\ldots,z^5).
\tag{1.1}
$$

令原十七个生成元按固定顺序为

$$
G_i(y,H)=\partial_{H_i}R_3\quad(0\le i\le10),
\qquad
G_{11+i}(y,H)=\partial_{y_i}R_3\quad(0\le i\le5).
\tag{1.2}
$$

先求全部原偏导，再代入 $y^\dagger$。此处 $H=M$，没有平移；六个原 $y$ 方向求导时 $H$ 保持独立。设

$$
g_i(M)=G_i(y^\dagger,M).
\tag{1.3}
$$

原均值的 catalecticant 是

$$
\operatorname{Cat}(y^\dagger)=
\begin{pmatrix}
2&1&1\\
1&1&1\\
1&1&1\\
1&1&2
\end{pmatrix}.
$$

取第 $0,1,3$ 行的三阶 minor 为 $1$，故其真秩为三。

本次小生成器重新由 literal $K$、原 $J_2,J_3$ 与完整 $J_3^{-1}$ 构造 (1.1)。六方向精确有理 dual 导数另与独立原 $N,\Gamma$ 收缩逐系数比较，全部

$$
17\cdot(1+11+66)=1326
$$

个坐标通过。$J_3^{-1}$ 的左右 512 个乘积坐标也全部实核。

十七条 $g_i$ 都是关于 $M$ 的次数至多二多项式，且**十七个常数项实际都非零**。因此以下始终保留常数目标。先前两原子点的零常数身份在此不适用。

对每条 $g_i$ 清常数有理分母与整数 content，得到

$$
g_i=\rho_i\widetilde g_i,\qquad
\rho_i\in\mathbb Q^\times,\quad
\widetilde g_i\in\mathbb Z[M].
\tag{1.4}
$$

全部 1326 个原有理坐标及其模 $127$ 运输都再次核对；十七个 $\rho_i$ 的分子、分母实际均为 $127$ 单位。这是同一原特殊纤维的合法常数行缩放。

## 2. 含常数的完整 $6188\times4368$ 原矩阵

取全部原来源

$$
M^\alpha\widetilde g_i,\qquad
|\alpha|\le3,\quad 0\le i\le16.
\tag{2.1}
$$

乘子数是 $1+11+66+286=364$，来源总数为 $6188$。目标为全部次数零至五的普通单项式：

$$
\mathcal V_{\le5}
=\operatorname{span}_{\mathbb Q}\{M^\beta:0\le|\beta|\le5\},
$$

$$
\dim\mathcal V_{\le5}=1+11+66+286+1001+3003=4368.
$$

每个 $g_i$ 次数至多二，故 (2.1) 全部原乘积都完整落在这个目标空间。常数、一次、二次乃至乘积的最高五次项全部保留，没有有限截断误差。

记其原行矩阵为

$$
\mathcal M^\dagger\in\mathbb Z^{6188\times4368}.
\tag{2.2}
$$

源顺序为乘子总次数、普通元组字典序、原方程编号；目标顺序为总次数零至五及普通元组字典序。native 从十七式的全部 78 个位置重建每个原来源；它不使用先前秩一或两原子模型的零来源筛选。

## 3. 实际满目标秩与特征零单位理想

实际完整结果为

$$
\boxed{
\operatorname{rank}_{\mathbb F_{127}}\overline{\mathcal M^\dagger}
=4368.
}
\tag{3.1}
$$

全部 $6188$ 行均构建并完成消元，保全尾部；每次消去后首非零位置严格后移。真实选行、原主元值及完整主元目标都保留在确定性 profile 中。

令 $R^\dagger$ 是实际选中的 $4368$ 个原来源标签，按原编号排序，并令

$$
B^\dagger=\mathcal M^\dagger[R^\dagger,:].
$$

实际原方块的排序符号与主元乘积给

$$
\boxed{\det\overline{B^\dagger}=61\ne0.}
\tag{3.2}
$$

故 $\det B^\dagger\ne0$，同原有理矩阵也满目标秩。取目标单项式列 $q(M)$，其第零条是常数 $1$，有

$$
\begin{pmatrix}
M^{\alpha_1}\widetilde g_{i_1}\\
\vdots\\
M^{\alpha_{4368}}\widetilde g_{i_{4368}}
\end{pmatrix}
=B^\dagger q(M).
$$

伴随恒等式的第零坐标给出确定的有限原来源

$$
\boxed{
1=
\sum_{k=1}^{4368}
\frac{\operatorname{adj}(B^\dagger)_{0k}}
     {\det B^\dagger\,\rho_{i_k}}\,
M^{\alpha_k}g_{i_k}(M).
}
\tag{3.3}
$$

每个原乘子次数至多三。因此

$$
\boxed{(g_0,\ldots,g_{16})=(1)\subset\mathbb Q[M].}
\tag{3.4}
$$

这是真理想等式，不仅是根式或点集排除。公式由原十七式与实际原选行完全确定；没有声称已经展开并永久保存全部巨大有理伴随矩阵。

原 Schur 变量

$$
Z=V+\frac14J_3^{-1}\ell
$$

保完整多项式理想身份

$$
(\nabla\mathcal Q_3)=(Z,\nabla R_3).
\tag{3.5}
$$

将 (3.5) 代入 $y^\dagger$，由 (3.4) 得完整原梯度理想也是单位理想。因此该均值下，无论 $H,V$ 取何值，都不存在完整原临界点。

## 4. 不特化均值的真实消去来源

现在保留六个独立均值变量 $y$。沿用实际点 (1.4) 的**固定常数** $\rho_i$，定义

$$
\widetilde G_i(y,H)=G_i(y,H)/\rho_i.
$$

不随参数重新取 primitive content。$G_i$ 关于 $H$ 仍是次数至多二的原多项式，系数属于 $\mathbb Q[y]$，其常数项一并保留。

用同一完整目标表、同一实际原选行 $R^\dagger$，构成

$$
\mathcal B(y)\in\operatorname{Mat}_{4368}(\mathbb Q[y]).
$$

令

$$
D(y)=\det\mathcal B(y).
\tag{4.1}
$$

在 $y=y^\dagger$ 时它就是 $B^\dagger$，故 (3.2) 严格证明 $D\ne0$。逐原来源有

$$
\big(H^{\alpha_k}\widetilde G_{i_k}(y,H)\big)_{k=1}^{4368}
=\mathcal B(y)q(H).
$$

其伴随公式第零坐标为

$$
\boxed{
D(y)=
\sum_{k=1}^{4368}
\frac{\operatorname{adj}(\mathcal B(y))_{0k}}
     {\rho_{i_k}}\,
H^{\alpha_k}G_{i_k}(y,H).
}
\tag{4.2}
$$

因此

$$
\boxed{
0\ne D(y)\in
(G_0,\ldots,G_{16})\cap\mathbb Q[y].
}
\tag{4.3}
$$

(4.2) 只使用原十七梯度，$H$ 乘子次数至多三；它不是把一个数值点的解直接搬成全参数解。原六变量全部保留在系数矩阵中，确定性选行不再改变。

局部化 $D$ 后原理想为单位理想。因此所有原完整临界均值都满足 $D(y)=0$，而

$$
\{D(y)\ne0\}\cap\{\operatorname{rank}\operatorname{Cat}(y)=3\}
$$

是一个明确非空的均值开集，包含 $y^\dagger$。

(3.5) 同样将 (4.3) 运回含十六个原 $V$ 的完整梯度理想。这里只给 reduced 原十七生成元的 $H$ 乘子次数三；不凭此填写经过 Schur 来源展开后的其他费用。

## 5. 原加权齐次性给 $\deg D=2643$

赋原权

$$
\operatorname{wt}(y_i)=1,\qquad
\operatorname{wt}(H_m)=2.
$$

由 (1.1)，$R_3$ 加权齐次六次。故原 $H$ 梯度权四，原 $y$ 梯度权五。来源 $H^\alpha G_i$ 的权为

$$
w_{\alpha,i}=2|\alpha|+
\begin{cases}4,&0\le i\le10,\\5,&11\le i\le16.\end{cases}
$$

目标 $H^\beta$ 权为 $2|\beta|$。其矩阵条目在 $y$ 中齐次次数为 $w_{\alpha,i}-2|\beta|$；负次数对应严格零条目。每个非零行列式项因而有共同均值次数

$$
\sum_{(\alpha,i)\in R^\dagger}w_{\alpha,i}
-\sum_{|\beta|\le5}2|\beta|.
\tag{5.1}
$$

对实际完整 profile 的原来源编号作独立只读计数，得到：

| 乘子次数 | 原 $H$ 梯度来源数 | 原 $y$ 梯度来源数 |
|---:|---:|---:|
| 0 | 11 | 6 |
| 1 | 121 | 66 |
| 2 | 606 | 380 |
| 3 | 1805 | 1373 |

总行数为 4368，原来源权和为 42683。完整目标权和为

$$
2(11+2\cdot66+3\cdot286+4\cdot1001+5\cdot3003)=40040.
$$

由 (3.2) 已知行列式不为零，故不是只给次数上界，而是

$$
\boxed{\deg_y D=42683-40040=2643.}
\tag{5.2}
$$

这个次数不表示已将 $D$ 的多项式系数全部展开。$D$ 是由有限原矩阵与实际选行定义的精确消去证书。

## 6. 与 Cat 异常集的准确关系

[完整两原子临界族](R150-appendix-nonzero-mean-zero-third-moment-critical-classification.md) 在每个有序不同两点参数上提供真实原临界点。把该族代入 (4.2)，即得 $D$ 在该整个两原子均值族上的恒等零值，也在其代数闭包上为零。这与前一 [两原子整纤维及参数开集证明](R150-appendix-original-two-atom-full-macaulay-rank4367-and-parameter-open-critical-ideal.md) 一致。

本稿尚未证明均值消去理想的根式等于 Cat minor 理想，也没有证明所有 Cat 秩三均值都满足 $D\ne0$。$D=0$ 内可能还有原临界参数；下一步应处理这个真正异常集及原消去理想，不能通过继续抽取孤立满秩点替代完整参数结论。

这一纤维为空，当然没有第三普通矩本质维数四、五、六的临界点。但这不把本点或本开集结论扩大为全原 Jacobian 自然幂、全均值分类或整体 ISP 结论。

## 7. 实际执行与全部原门

小模型和完整秩计算都在授权后的独占本地临时目录执行。源码在执行前冻结，均为真实运行，**没有 GitHub Actions run ID**。

小模型耗时 **0.678244285 秒**，精确原系数门通过。完整 wrapper 耗时 **51.199731137 秒**，含编译 **4.360027085 秒**；native 自报 **45.1511 秒**，native 外墙 **45.188373455 秒**。全部程序 exit 0。

| 实际门 | 结果 |
|---|---:|
| 原 Cat 均值秩 | 3 |
| 原 $J_3^{-1}$ 双边乘积 | 512 坐标全真 |
| 独立原 $N,\Gamma$ 梯度系数 | 1326 坐标全真 |
| primitive 原有理运输 | 1326 坐标全真 |
| 原模 $127$ 系数运输 | 1326 坐标全真 |
| 十七常数项 | 全部保留，实际都非零 |
| 原来源 | 6188，全部完成 |
| 目标，包括常数 | 4368，全部保留 |
| 独立位面算术 | 244990 检查全真 |
| 实际行消元 | 13398162 次 |
| 规范原主元 | 4368 |
| 原排序 minor | 模 $127$ 为 61 |
| 完整有限域余空间 | 零维 |
| 末 checkpoint | generation 6，phase 3 完成 |

零维核的乘回坐标数是零；其真空完成标记不是满秩的独立算术证据。满秩证据是完整原来源消元与非零原 minor (3.2)。

### 7.1 冻结源码及参数

| 文件 | Git blob | B | SHA256 |
|---|---|---:|---|
| [原 Cat 秩三生成器](../notes/2026-11-16-r150-original-nonrankone-cat-rank-three-gradient-789f.py) | 11f058f7d53a9914478f1dd051b887e4342eb9b0 | 19879 | ab088528d828c51136a5746236735d51f2ed22934ccad8c8623dfb29f0090a8f |
| [完整 native](../notes/2026-11-16-r150-original-nonrankone-cat-rank-three-macaulay-native-789f.cpp) | 592bcfb834a30e6bfcc39dcd8a38ce9dfa9782d1 | 17996 | 0d53f3472c0250459da9091a16151f70ca2011c7b99962ef12c84ede62b66d92 |
| [完整 wrapper](../notes/2026-11-16-r150-original-nonrankone-cat-rank-three-macaulay-rank-789f.py) | a215806be2b019c61d027f5d3dae6005eac8c4f2 | 22522 | 50520960e23026c4a3a88c856e321772468d538239eba835b41fa046adf0c822 |
| [七位面 header](../notes/2026-11-15-r150-original-f127-bitplane-789f.hpp) | 796c0d4c790b3f2294bc203f057e78c0fb16d4ed | 4691 | 03272796bb20c883291d27c9a0b796197f8295ccd9b16552c13894657dc8afd3 |

[独立 inputs](../notes/2026-11-16-r150-original-nonrankone-cat-rank-three-macaulay-inputs-789f.json) 与 [接口](../notes/2026-11-16-r150-original-nonrankone-cat-rank-three-macaulay-interface-789f.md) 给全部 180 秒、2048 MiB、编译 30 秒参数及完整协议。具体本地执行身份保存在 [manifest](../notes/r150-nonrankone-execution-789f/20261116-local-cat-rank-three-complete-macaulay-rank.json)。

### 7.2 实际逻辑数据及输出 SHA

原精确模型逻辑数据为 159454 B，SHA256：

~~~text
c05317c3fe6ac9342260fe08615d80ff8e21637f03969b80584282bf4848f48d
~~~

原输入为 12114 B，SHA256：

~~~text
704d987062e58108cb825246022fffecb45e9d68641ef83138a48386d33d592d
~~~

完整来源字典、完整含常数目标字典、实际原选行标签的 SHA256 分别是：

~~~text
615ac544fb4111e77fa4c4d21e43557027092a58b72d36b3c7f02434083ea14d
a9b637e190c4cbb903085b67d1b2834bddd162479e8713b2bba179ffbdf5bad0
7490f46ca82f8367181dd084beac0c4cd3afb677f4aef01e5b5bb5101738b5d7
~~~

实际完整 profile 为 41823 B，SHA256：

~~~text
aae42843c014c402704b18c13dcc41150c572bc934341b81e16dec78677f390c
~~~

完整临时小回执为 9208 B，SHA256：

~~~text
a1aff8a4a0a39f3b68c18874802e8d3eecf9df8a387cf21a635ca84984dff972
~~~

语义 binding：

~~~text
36b9c974fbf4714804204afc3c6798753ebb79a4917ba76da1beda69b6a1b5b7
~~~

按规则15，矩阵、profile、完整核、两槽状态均只在临时目录；仓库仅保存源、参数、执行身份、输出 SHA 与证明。所有选行和源字典都可从这些冻结入口确定性重建。
