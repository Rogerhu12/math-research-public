# R294 附录：原连续尾的坐标平移、八次条件数与十四次第一返回锚

日期：2026-11-14 UTC。作者：Astra-ISP-789f。

**状态：以下原模型估计已证明。** 将 [R294 全高度对角比较](R294-birth-one-uniform-diagonal-gram-comparison-and-common-newton-blocks.md)接到原连续权的准确坐标平移，把 [R271 原出生一旧列稿](R271-appendix-original-birth-one-all-height-polynomial-first-return-anchor.md) 的平方费用幂次 61 改进为 28。下面保持该稿同一个真幂 MP、同一出生商及全部乘法次序。高出生、完整 graph 跨出生以及无指定速率锚的传播仍未支付。

## 1. 原权行与准确归一

固定 $m\ge1$，写
$$
x=m+1,\qquad b_i=(i+1)^{-2}\ (i\ge m),\quad
w_i=b_i^2,\quad S=S_m=\sum_{i\ge m}w_i,
$$
$$
D=\sum_{i\ge m}b_iE_i,\quad K=b^\perp,\qquad
J_t=(D^t:\mathcal H_{t+1}\to\mathcal H_1)^\dagger|_K,
\qquad H_t=J_t^*J_t,\quad H_0=I_K.
$$
令 $e_t=e_t(w)$，$e_0=1$，并置
$$
\boxed{\sigma_t=(t!)^2e_t,\qquad
R_t=\left(\frac{x+t}{x}\right)^4,\qquad
\alpha_t=R_tR_{t+1}.}
\tag{1.1}
$$
注意原真幂 $D^t$ 的 Gram 为
$$
H_t=(t!)^{-2}\Gamma_t,
$$
其中 $\Gamma_t$ 才是 R294 中归一幂 $D^t/t!$ 的 Gram。所有完整逆与无限固定高度的合法性由该稿 §5 和原 R271 §2 支付，不互换逆与压缩。

本稿的基本夹逼是
$$
\boxed{\frac1{2\sigma_t}I_K\preceq H_t
\preceq\frac{\alpha_t}{\sigma_t}I_K.}
\tag{1.2}
$$
因此
$$
\boxed{\frac{\sigma_t}{\alpha_t}I_K\preceq H_t^{-1}
\preceq2\sigma_tI_K,\qquad
\operatorname{cond}(H_t)\le2\alpha_t
\le2(t+1)^4(t+2)^4.}
\tag{1.3}
$$
$t=0$ 时真实 $H_0=I$，(1.2) 是合法但不取等的夹逼。

## 2. 删除任一物理位的坐标平移界

把平方权重新标为 $w_j=j^{-4}$，$j\ge x$。对任意 $t$ 元指标集 $I=\{j_1<\cdots<j_t\}$，同时右移一个位置，得到
$$
\frac{\prod_{r=1}^t w_{j_r}}{\prod_{r=1}^t w_{j_r+1}}
=\prod_{r=1}^t\left(1+\frac1{j_r}\right)^4
\le\prod_{r=1}^t\left(\frac{x+r}{x+r-1}\right)^4
=R_t.
$$
这里 $j_r\ge x+r-1$，每个比值随 $j_r$ 递减。指标右移是所有 $j\ge x$ 的 $t$ 元集到所有 $j\ge x+1$ 的 $t$ 元集的双射。因此对非负绝对收敛级数求和，
$$
e_t(w\text{ 删除首位})\ge e_t/R_t.
$$
删除任一其他位后，按从大到小排列的剩余权逐坐标不小于删除首位后的权，故其初等对称和不小于后者。于是对每个物理 $i$，
$$
\boxed{\frac{e_t}{R_t}\le e_t^i\le e_t,
\qquad e_t^i=e_t(w\text{ 删除 }i).}
\tag{2.1}
$$
$t=0$ 同样成立。

R294 的共同对角系数是
$$
g_{t,i}=\frac{e_{t+1}}{e_t^i e_{t+1}^i}.
$$
应用 (2.1) 于两个高度，得
$$
\boxed{\frac1{e_t}\le g_{t,i}\le\frac{R_tR_{t+1}}{e_t}.}
\tag{2.2}
$$
用同一个 $K$ 压缩，并代入 $A_t/2\preceq\Gamma_t\preceq A_t$，再恢复 $t!$，即得 (1.2)–(1.3)。这里不需要对删位矩阵建立相邻序。

## 3. 新标量尺度的相邻比

记 $S_y=\sum_{j\ge y}j^{-4}$，因此 $S=S_x$。原正计数身份给
$$
t e_t=\sum_{|I|=t-1}w_I\sum_{j\notin I}w_j.
$$
任意删去 $t-1$ 个位置后，总质量在 $S_{x+t-1}$ 与 $S$ 之间，所以
$$
\frac{S_{x+t-1}}t\le\frac{e_t}{e_{t-1}}\le\frac St.
$$
由 (1.1)，
$$
\boxed{tS_{x+t-1}\le\frac{\sigma_t}{\sigma_{t-1}}\le tS
\qquad(t\ge1).}
\tag{3.1}
$$

积分比较给
$$
\frac1{3y^3}\le S_y\le\frac1{3(y-1)^3}\quad(y\ge2).
$$
由于 $x\ge2$，
$$
\boxed{\frac{S}{S_{x+t-1}}
\le\left(\frac{x+t-1}{x-1}\right)^3
\le(t+1)^3.}
\tag{3.2}
$$
这些是同一原尾的真实标量费用，不是任意正权行的普适比值。

## 4. 完整非交换旧列乘积的改进

对整数 $h\ge1$、$1\le\ell\le h$，保持原乘积次序：
$$
\mathcal M_{h,\ell}
=H_{h-1}H_h^{-1}H_\ell H_h^{-1}H_{h-1}.
$$
先用 (1.2) 逐次估计算子范数，再用同一式把单位矩阵换回原 $H_{\ell-1}$，得到
$$
\boxed{\mathcal M_{h,\ell}\preceq
8\alpha_{h-1}^{,2}\alpha_\ell
\left(\frac{\sigma_h}{\sigma_{h-1}}\right)^2
\frac{\sigma_{\ell-1}}{\sigma_\ell}\,H_{\ell-1}.}
\tag{4.1}
$$
因子八分别来自两个 $H_h^{-1}\preceq2\sigma_h I$ 以及
$I\preceq2\sigma_{\ell-1}H_{\ell-1}$。没有交换 $H_t$ 或把它们当作共同对角矩阵。

(3.1) 先给保留原 $m$ 依赖的较锐形式
$$
\boxed{\mathcal M_{h,\ell}\preceq
8\alpha_{h-1}^{,2}\alpha_\ell\frac{h^2}{\ell}
\frac{S^2}{S_{x+\ell-1}}\,H_{\ell-1}.}
\tag{4.2}
$$
再用 $R_t\le(t+1)^4$ 和 (3.2)，系数至多
$$
8\,\frac{h^{10}(h+1)^8(\ell+1)^7(\ell+2)^4}{\ell}\,S.
$$
因为 $(\ell+1)/\ell\le2$ 且 $\ell\le h$，得到统一的
$$
\boxed{\mathcal M_{h,\ell}
\preceq16(h+2)^{28}S_m\,H_{\ell-1}.}
\tag{4.3}
$$
这取代原 R271 (1.6) 中的 $(h+2)^{61}S_m$。不是把一个未证的矩阵 Newton 命题当作中间步骤。

## 5. 原第一下降伴随、最高锚及新列

原同一出生商的真 MP 字典为
$$
D_1J_t=J_{t-1},\qquad
D_1^*J_{h-1}=J_hH_h^{-1}H_{h-1}.
$$
若 $y=J_{h-1}u$，对 $0\le j<h$ 置 $\ell=h-j$，则
$$
\|D_1^jD_1^*y\|^2
=\langle\mathcal M_{h,\ell}u,u\rangle,
\qquad
\|D_1^jy\|^2=\langle H_{\ell-1}u,u\rangle.
$$
故对任意非负列权 $c_0,\ldots,c_{h-1}$，
$$
\boxed{\sum_{j<h}c_j^2\|D_1^jD_1^*y\|^2
\le16(h+2)^{28}S_m\sum_{j<h}c_j^2\|D_1^jy\|^2.}
\tag{5.1}
$$

当原截断头高度 $d=2^m$、$h=d$ 时，没有新增的 $j=d$ 列。沿原定义
$$
\Theta_d=\sum_{j<d}v_j^2(D_1^j)^*D_1^j,
\qquad
\Theta_{d+1}^{[d]}=\sum_{j<d}v_j^2(D_1^j)^*D_1^j
$$
（第二式作用于输出高度），(5.1) 直接给
$$
\boxed{\|(\Theta_{d+1}^{[d]})^{1/2}D_1^*y\|
\le4(d+2)^{14}\sqrt{S_m}\,\|\Theta_d^{1/2}y\|
\le\frac{4(d+2)^{14}}{\sqrt3\,m^{3/2}}\,\|\Theta_d^{1/2}y\|.}
\tag{5.2}
$$
这在原整个出生一和所有合法出生商参数 $q$ 上成立。

若 $h<d$，新列仍须单独保留。由同一夹逼和 (3.1)，
$$
\|H_h^{-1}H_{h-1}\|^2
\le4\alpha_{h-1}^{,2}\left(\frac{\sigma_h}{\sigma_{h-1}}\right)^2
\le4h^{10}(h+1)^8S_m^2
\le4(h+1)^{18}S_m^2.
$$
因此准确新列满足
$$
\boxed{\|D_1^hD_1^*y\|^2
\le4(h+1)^{18}S_m^2\|D_1^{h-1}y\|^2.}
\tag{5.3}
$$
加入其原加权费用时，仍须支付 $v_h/v_{h-1}$；(5.1) 没有免费包括新列。

## 6. 未扩大的范围

本稿只改进原连续尾出生一的完整条件数与第一返回费用。一般出生 $a\ge2$、$\Gamma^{-1}$ 的跨出生传播、固定物理测试的完整双费 Gram 和边界 $N=M$ 均未关闭。原最高正锚只有无指定速率的趋零；即使幂次降为十四，仍不能无条件乘上它而宣布传播消失。准确的 $m,h,\ell$ 依赖已保在 (4.2)，后续若使用须在同一实际源上另付所需速率。
