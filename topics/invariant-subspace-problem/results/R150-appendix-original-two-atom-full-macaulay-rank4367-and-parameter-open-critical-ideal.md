# 原非秩一两原子纤维的完整 Macaulay 秩 4367 与参数开集原理想等式

作者：Astra-ISP-789f / normal_annihilator。AI-assisted: GPT-6 Astra Pro。  
日期：2026-11-16 UTC。

状态：**已证明；原完整有限矩阵实际计算已完成。** 固定真正秩二均值 $y_*=e_0+e_5$ 后，全部原十七个梯度的理想恰为平移变量的极大理想 $(m_0,\ldots,m_{10})$。本次证明保留全部 $6188$ 个原来源与全部 $4367$ 个正次数至多五目标；模 $127$ 的真实原 minor 为 $55\ne0$，从而得到特征零的整个固定均值结论。每个 $m_j$ 都有乘子次数至多三的原来源。

同一组原来源还给两原子参数图上的一个**只依赖参数的**非零 minor。局部化该 minor 后，每个参数纤维的全部原临界点都等于原两原子值，方案也约化。这里不再需要先前依赖 $M$ 的局部行列式条件；尚未处理该参数 minor 的零集或 Cat 均值秩三部分。

## 1. 原模型与先求导后限制

使用 [完整第三矩 Schur 模型](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md) 的同一个原矩阵

$$
K=
\begin{pmatrix}
0&0&0&0&5&-1\\
0&0&0&-32&5&-1\\
0&0&54&-4&5&0\\
0&-32&-4&-8&0&0\\
5&5&5&0&0&0\\
-1&-1&0&0&0&0
\end{pmatrix},
\qquad v(z)=(1,z,\ldots,z^5)^{\mathsf T}.
$$

原变量为六个 $y_i$ 与十一条 Hankel 坐标 $H_m$。令

$$
F=\frac12y^{\mathsf T}Ky,\quad p=Ky,\quad
b=p^{\mathsf T}Hp,\quad c=p^{\mathsf T}HKHp,\quad
\tau_j=\operatorname{tr}((KH)^j).
$$

令 $J_3$ 为二变量多项式
$(v(z)^{\mathsf T}Kv(w))^3$ 的 $16\times16$ 系数矩阵，并令

$$
\ell_m=[z^m](p^{\mathsf T}v(z))^3
-6[z^m]\big(v(z)^{\mathsf T}KHKv(z)\big)(p^{\mathsf T}v(z)).
$$

同原 Schur 多项式为

$$
R_3=F^3-6Fb+6F\tau_2+12c-8\tau_3
-\frac12\ell^{\mathsf T}J_3^{-1}\ell.
\tag{1.1}
$$

原十六个三阶变量记为 $V$。变换

$$
Z=V+\frac14J_3^{-1}\ell
$$

是多项式三角坐标变换，并保留已证明的完整梯度理想身份

$$
(\nabla\mathcal Q_3)=(Z,\nabla R_3).
\tag{1.2}
$$

取

$$
y_*=e_0+e_5,\qquad
H_*=\frac12(e_0e_0^{\mathsf T}+e_5e_5^{\mathsf T}),\qquad
V_*=\frac12(e_0^{\otimes3}+e_5^{\otimes3}).
\tag{1.3}
$$

$y_*$ 的 $4\times3$ Hankel catalecticant 秩为二；它对应原曲线两个不同射影点 $0,\infty$。写

$$
H=H_*+M,\qquad M_{ij}=m_{i+j}.
$$

定义十七个原式

$$
F_i(M)=
\left.\frac{\partial R_3}{\partial H_i}\right|_{y_*,H_*+M}
\quad(0\le i\le10),
$$

$$
F_{11+i}(M)=
\left.\frac{\partial R_3}{\partial y_i}\right|_{y_*,H_*+M}
\quad(0\le i\le5).
\tag{1.4}
$$

**所有偏导先在原变量中求完，然后才代入。** 特别是六个 $y$ 导数中的 $H_*$ 保持固定，没有把沿两原子参数的导数替代原梯度。

[前一原十一阶 minor 证明](R150-appendix-original-two-atom-nonrankone-linear-minor-and-local-source-certificate.md) 已逐全部 $1326$ 个次数至多二系数核对 (1.4) 与独立原 $N,\Gamma$ 公式，也已核十七常项全部为零。此处重新运行同一个生成器，核其完整逻辑模型 SHA 相同，并再次逐全部 $1309$ 个非恒定坐标运输到 primitive 整数式：

$$
F_i=\rho_i\widetilde F_i,\qquad
\rho_i\in\mathbb Q^\times.
\tag{1.5}
$$

每个 $\rho_i$ 的分子、分母都实际为 $127$ 单位。没有除去一个 $127$ 因子后改变原特殊纤维。

## 2. 全部原来源到完整有限目标空间

令

$$
\mathcal V_5=
\operatorname{span}_{\mathbb Q}
\{m^\beta:1\le|\beta|\le5\}.
$$

其完整普通单项式基的大小为

$$
11+66+286+1001+3003=4367.
$$

全部原来源为

$$
m^\alpha\widetilde F_i,\qquad
|\alpha|\le3,\quad 0\le i\le16.
\tag{2.1}
$$

乘子共有 $1+11+66+286=364$ 个，因此原来源总数为

$$
17\cdot364=6188.
$$

每个 $\widetilde F_i$ 次数至多二、常项零，所以 (2.1) 的每个原项都完整落在 $\mathcal V_5$ 中。这里没有截去高于五的项，也没有遗漏常项约束。

记行表示矩阵为

$$
\mathcal M_*\in\mathbb Z^{6188\times4367}.
\tag{2.2}
$$

源顺序是乘子总次数、普通变量元组字典序，再按原方程编号 $0,\ldots,16$；目标顺序是总次数一至五及普通元组字典序。native 从十七式的全部 $17\cdot77=1309$ 个一、二次位置重建每条来源，不使用旧秩一 NF 的预筛字典，不丢弃任何“已知零来源”。

这与将来源作列的 $4367\times6188$ 原 Macaulay 映射互为转置。以下始终使用 (2.2) 的行 convention。

## 3. 实际完整有限域秩与原非零 minor

固定素数为 $127$。实际结果为

$$
\boxed{\operatorname{rank}_{\mathbb F_{127}}\overline{\mathcal M_*}=4367.}
\tag{3.1}
$$

全部 $6188$ 条原行已构建并完成消元；不是在先取得局部秩后忽略剩余来源。消元保留每行的完整尾部，每次消去后首非零位置严格后移。主元位置、选中的原来源编号与规范前主元值都保存在可重建完整 profile 中。

令 $R$ 为该确定性算法实际选中的 $4367$ 个原来源标签，并按原编号排序。所有 $4367$ 个目标列均保留。记所选方块为

$$
B_*=\mathcal M_*[R,:].
$$

以原排序计，实际主元乘积及行置换符号给

$$
\boxed{\det\overline{B_*}=55\in\mathbb F_{127}^\times.}
\tag{3.2}
$$

因此 $\det B_*$ 是非零整数，$\operatorname{rank}_{\mathbb Q}\mathcal M_*=4367$。结合 (1.5)，这是同十七个原导数的特征零满目标秩；不是从有限域未满秩推特征零负结论。

本次 free-I 核有零列。其“全部原核乘回”计数因而为零，不能把这个真空检查当作证明满秩的算术证据。满秩证据是全部原行实际消元以及 (3.2) 的真实非零原 minor。位面算术另有 $244990$ 个独立标量检查全部通过。

## 4. 固定均值的整个原理想恰为 $(M)$

将完整目标单项式列写为 $q(M)$。设第 $k$ 个选中来源标签是 $(\alpha_k,i_k)$，则在原有理多项式环中逐系数有

$$
\begin{pmatrix}
m^{\alpha_1}\widetilde F_{i_1}\\
\vdots\\
m^{\alpha_{4367}}\widetilde F_{i_{4367}}
\end{pmatrix}
=B_*q(M).
\tag{4.1}
$$

令 $\nu(j)$ 是目标基中 $m_j$ 的实际位置。伴随恒等式给确定的有限原来源公式

$$
\boxed{
m_j=
\sum_{k=1}^{4367}
\frac{\operatorname{adj}(B_*)_{\nu(j),k}}
     {\det B_*\,\rho_{i_k}}\,
m^{\alpha_k}F_{i_k}(M).
}
\tag{4.2}
$$

所以每个 $m_j$ 都由全部原梯度生成，来源系数的 $M$ 次数至多三。公式 (4.2) 由原十七式、实际原行标签和普通伴随矩阵完全确定；没有另作来源假设。此处不声称已将 $4367$ 阶有理逆的所有系数材料化保存。

所有 $F_i(0)=0$，故反向包含显然成立。于是

$$
\boxed{
(F_0,\ldots,F_{16})=\mathfrak m:=(m_0,\ldots,m_{10})
\quad\text{在 }\mathbb Q[M]\text{ 中}.
}
\tag{4.3}
$$

这已覆盖固定 $y_*$ 的**全部** $M$，包括前一局部行列式 $\det C(M)=0$ 的点。其原临界方案是一个约化点。

将 (1.2) 同时限制到该固定均值，得到完整原理想

$$
(\nabla\mathcal Q_3)\big|_{y=y_*}=(M,Z).
\tag{4.4}
$$

因此全部二、三阶变量必为 $H_*,V_*$。原完整第三普通矩

$$
T_3(r)=(r^{\mathsf T}y)^3
-6(r^{\mathsf T}y)(r^{\mathsf T}Hr)+4V(r,r,r)
$$

恒为零，所有原匹配方向的 Bell 值也为零。特别是这个真正非秩一固定均值纤维不含第三矩本质维数四、五、六的临界点。

## 5. 只依赖两原子参数的原来源 minor

取原有序两原子参数图

$$
u(s)=(1,s,\ldots,s^5),\qquad
w(t)=(t^5,t^4,\ldots,1),
$$

$$
x=a\,u(s),\qquad z=b\,w(t),\qquad ab(1-st)\ne0.
$$

两个物理曲线点不同，幅度都非零。令

$$
y=x+z,\qquad
H_0=\frac12(xx^{\mathsf T}+zz^{\mathsf T}),\qquad
V_0=\frac12(x^{\otimes3}+z^{\otimes3}).
\tag{5.1}
$$

[原完整零第三矩分类](R150-appendix-nonzero-mean-zero-third-moment-critical-classification.md) 已证明这整个两原子族属于原临界理想。故先对 $R_3$ 求原十七偏导、再代入 $y,H_0+M$ 得到的

$$
\mathcal F_i(a,b,s,t;M)
$$

具有恒零的 $M$ 常项，并且 $M$ 次数至多二。所有系数属于 $\mathbb Q[a,b,s,t]$；这里 $J_3^{-1}$ 只有固定有理常数。

**始终沿用实际基点 (1.5) 的固定常数 $\rho_i$。** 不在不同参数处重新除 content，也不引入一个可能消失的参数行因子。用 $\mathcal F_i/\rho_i$、同一完整目标字典与实际选中原来源标签 $R$，定义方块

$$
\mathcal B(a,b,s,t)
\in\operatorname{Mat}_{4367}\big(\mathbb Q[a,b,s,t]\big).
$$

令

$$
D(a,b,s,t)=\det\mathcal B(a,b,s,t).
\tag{5.2}
$$

在 $(a,b,s,t)=(1,1,0,0)$，它就是 $B_*$。由 (3.2)，$D$ 是非零多项式。它完全不依赖 $M$。因此

$$
U=\{ab(1-st)D(a,b,s,t)\ne0\}
\tag{5.3}
$$

是有序两原子参数图中的明确非空主开集。

同 (4.1) 的原来源身份及伴随公式给

$$
\boxed{
D\,m_j=
\sum_{k=1}^{4367}
\frac{\operatorname{adj}(\mathcal B)_{\nu(j),k}}
     {\rho_{i_k}}\,
m^{\alpha_k}\mathcal F_{i_k}.
}
\tag{5.4}
$$

右侧每个原来源乘子的 $M$ 次数仍至多三。将 $D$ 逆化后，

$$
\boxed{
(\mathcal F_0,\ldots,\mathcal F_{16})
=(M)
\quad\text{在 }\mathbb Q[a,b,s,t,(ab(1-st)D)^{-1}][M]\text{ 中}.
}
\tag{5.5}
$$

加入原 Schur 变量后，完整拉回理想就是 $(M,Z)$。所以 $U$ 内每个参数的整个原临界纤维都是 (5.1)，不存在另一个非零 $M$ 分支，且无非约化结构。

这里“拉回”指把原梯度代入参数图，**不是对拉回的标量多项式重新只取四个参数导数**。该区别保留全部原十七方向。

## 6. 结果范围与尚未处理的部分

由 (4.3) 已得到固定均值 $e_0+e_5$ 的完整分类。由 (5.5) 又得到有序两原子图中的非空参数开集，且每个纤维完整。

本稿尚未证明 $D$ 在整个约化 Cat 秩二参数区上是单位，也没有处理 $D=0$ 的其他参数纤维、合流两点均值或 Cat 秩三均值。它不把一个参数主开集扩大为全局原 Jacobian 幂理想，不宣称该参数多项式对应的算子已有逆。

对于匹配 Bell 方向，(4.4)–(5.5) 给该范围内原 Bell 形式的一次成员性及零值；这里没有把原 rank-one 的来源费用直接搬到新图，也没有给出整个 Hilbert 空间问题的收口。

## 7. 本地实际执行与可重现身份

这次完整矩阵计算是父任务明确授权后的**本地 executor 实际运行**，不是 GitHub Actions job。运行目录为临时独占目录；代码与参数均在运行前冻结，运行后没有替换数学源码。

执行身份见 [只含源、参数、执行身份及输出 SHA 的 manifest](../notes/r150-nonrankone-execution-789f/20261116-local-two-atom-complete-macaulay-rank.json)。它明确记录 GitHub run 为 null。实际运行使用 Python 3.12.14、python-flint 0.9.0、g++ 14.2.0；编译与数学都成功，exit 0。

| 实际检查或结果 | 值 |
|---|---:|
| 原方程 | 17，全部保留 |
| 原来源 | 6188，全部构建并消元 |
| 完整正次数目标 | 4367，全部保留 |
| 原有理行比例乘回 | 1309 个坐标全真 |
| 原模 $127$ 行比例乘回 | 1309 个坐标全真 |
| 十七行比例 | 分子、分母均为 $127$ 单位 |
| 位面独立算术检查 | 244990，全真 |
| 完整规范主元 | 4367 |
| 实际有限域余空间 | 零维 |
| 原选中 minor | $\det\bmod127=55$ |
| 完整行消元次数 | 12171626 |
| 最终 checkpoint | generation 6，完成 phase 3 |

时间分别为：

- wrapper 总用时 **48.971448746 秒**，包含编译；
- 编译 **5.329987838 秒**；
- 原有理模型重建 **0.954790230 秒**；
- native 自报 **42.4378 秒**，native 外墙 **42.476624946 秒**。

未测量实际峰值 RSS；2048 MiB 是有界运行限制，不冒充实测用量。实际核数组只有零列，见 §3 的证据区分。

### 7.1 四个冻结源码

| 文件 | Git blob | B | SHA256 |
|---|---|---:|---|
| [原十七式生成器](../notes/2026-11-16-r150-original-nonrankone-two-atom-gradient-789f.py) | 948d3c17f90ee17c9b0b773d981c3189674b47d5 | 22167 | 3729a351a361039e286b2435571da8c2c91d09d9822cc79cacb9cecf887928cc |
| [完整秩 wrapper](../notes/2026-11-16-r150-original-nonrankone-two-atom-macaulay-rank-789f.py) | 3578bb14b721a0e850fdba310c592937ddd66367 | 22077 | c2d85cbef4611516ddaf462d85f10319a36381bd5deb8bf8ffc562eea84bc3d9 |
| [原矩阵 native](../notes/2026-11-16-r150-original-nonrankone-two-atom-macaulay-rank-native-789f.cpp) | e22e55f6e3175e4ac7b9b759c5420fccda39a949 | 17882 | a09439dd1e68b737b09d09d792158f6cd48ce8c6bad4e899746e584ef4822099 |
| [七位面 header](../notes/2026-11-15-r150-original-f127-bitplane-789f.hpp) | 796c0d4c790b3f2294bc203f057e78c0fb16d4ed | 4691 | 03272796bb20c883291d27c9a0b796197f8295ccd9b16552c13894657dc8afd3 |

[冻结参数](../notes/2026-11-16-r150-original-nonrankone-two-atom-macaulay-rank-inputs-789f.json) 与 [完整协议接口](../notes/2026-11-16-r150-original-nonrankone-two-atom-macaulay-rank-interface-789f.md) 保留全部 CLI、预算、两槽恢复与未满秩分支。此次没有触发预算续接。

### 7.2 实际输入、原字典和输出身份

模型解压后的逻辑数据为 173045 B，SHA256：

~~~text
1f93dcd7db76f433df57536d4bd0b51417ae2a12137e08136141b4a9689a8d8d
~~~

它与先前 Actions 小门的全部逻辑字节相同。不同 Python 版本的 gzip 头不作为数学身份；没有将本次压缩文件伪记成旧压缩 SHA。

完整来源字典、完整目标字典及实际选中原来源标签的 SHA256 分别为：

~~~text
615ac544fb4111e77fa4c4d21e43557027092a58b72d36b3c7f02434083ea14d
7f56a412a0f898d4f8fe7afb393aec1069e006344d293e00c3c36e5db9d55752
21b5de896cb9e24b2b19179b96fdd49d5cbacc185d2ca5fde450e9531da4d851
~~~

实际原输入为 11961 B，SHA256：

~~~text
b900414237edf13be24654492ad51991f2b140360a1abf97f8db3fa4c362421f
~~~

完整临时 profile 为 41808 B，SHA256：

~~~text
ebe6f69b16c5f7cc09f751cb2ce2a9f02cb8f6441951f18f19223c72a6644957
~~~

实际完整小回执为 7454 B，SHA256：

~~~text
190d134f3c6e8dba737b89f563289f6d46f29f539e4130d04acbe1f82a505208
~~~

语义 binding 为：

~~~text
bdbe6a519646adbdc0013e1e2ef8f7689894214ee372a6213e3a45f70c65d672
~~~

按仓库规则15，原矩阵、完整 profile、核数组和两槽状态均只在临时目录；仓库保存可重现的源码、参数、执行身份、输出 SHA 与本证明。定理所用原选行通过冻结算法及全部输入确定，不将临时数组缺席变成一个未说明的来源选择。
