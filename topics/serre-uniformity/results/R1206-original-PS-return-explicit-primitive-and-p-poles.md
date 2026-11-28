# R1206：原 PS 返回的显式原函数与不可删除的 p 阶极点

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；root / global_route。

**已证明的范围。** R1204 的实际 high-PS 返回微分不仅被 Cartier 杀掉，而且有同一个原 Igusa 曲线上的显示有理原函数。该函数在三个 CM 端点和所有无穷远点正则消失；其全部极点在原 SS 集，阶至多 $p$。这些 $p$ 阶极点是原函数的实际部分，不能因其模 $p$ 微分为零而删掉，也不能据 exactness 宣称原 Abel 对数或完整 Čech 配对为零。

## 1. 原对象与准确恒等式

沿 R1193、R1200、R1204，保持
$$
p=12g-1>37,\quad n=2g-1,\quad m=3n+2,\quad p=6n+5,
$$
$$
r=1-b^3,\qquad A=bQ(b^3),\qquad
h=r^{n+1}A,\qquad u^m=h.
\tag{1206.1}
$$
全部等式在原约化曲线的函数域中进行，$k$ 为原剩余域。$A$ 的根简单，且与 $r$ 无共同根。原 PS 参数为
$$
T\in b^2k[b^3]_{\le n-1},\qquad \deg_b T\le m-2.
$$
写
$$
\mathscr DT=rT''-4b^2T'-\frac94 bT,
\qquad
f_T=\frac r u\left(\frac T A\right)' .
\tag{1206.2}
$$
这里的撇号均为原坐标 $b$ 的导数，不是 ordinary quotient 的新参数导数。准确有
$$
\boxed{\quad
df_T=\frac{\mathscr DT}{uA}\,db.
\quad}
\tag{1206.3}
$$
因此 R1204 的实际返回 $C(T)=-3\gamma^2\mathscr DT$ 满足
$$
\boxed{\quad
\eta_{C(T)}=\frac{C(T)}{uA}\,db
          =-3\gamma^2\,df_T.
\quad}
\tag{1206.4}
$$
$\gamma$ 是同一原 Igusa–Weil 相位；没有重新选择或反除一个未知单位。

## 2. 从原 Jacobi 方程逐项推导

R1201／R1204 的原 $Q(B)$ 满足
$$
B(1-B)Q''+\frac43(1-2B)Q'-\frac{25}{36}Q=0.
$$
代入 $A=bQ(b^3)$，直接链式法则给
$$
\boxed{\quad rA''+\frac43r'A'=\frac94 bA.\quad}
\tag{1206.5}
$$
例如左边除以 $b^2$ 后是
$9B(1-B)Q''+12(1-2B)Q'-4Q$，原方程将其化为 $9Q/4$；恒等式为多项式式，因此也在 $b=0$ 成立。

在特征 $p$ 中，$m=-1/2$、$n=-5/6$，故
$$
\frac{u'}u=-2\frac{h'}h,
\qquad
2n+3=\frac43.
$$
置 $F=T/A$。于是
$$
df_T=\frac1u\left[rF''+
 \left(\frac43r'+2r\frac{A'}A\right)F'\right]db.
$$
展开 $F$ 后，所有 $T'$ 项中含 $A'/A$ 的部分相消，所有 $T$ 项中含 $(A'/A)^2$ 的部分亦相消。剩下
$$
df_T=\frac1{uA}\left[
rT''+\frac43r'T'
-\frac{rA''+(4/3)r'A'}A T\right]db.
$$
用 $r'=-3b^2$ 及 (1206.5) 即得 (1206.3)。这项推导完全在同一原函数域中完成；它没有从 Cartier 核的维数反推一个未构造的原函数。

## 3. 全部极点与精确 SS 主部

### 3.1. SS 点：一个 p 阶项与一个简单项

令 $s$ 为原 $A$ 的任一根。原局部参数取
$$
W=u/\tau_s,
$$
其中 $\tau_s$ 是 R1200 的同一个实际单位。由 (1206.1)，
$$
A=\frac{\tau_s^m W^m}{r^{n+1}},\qquad
b-s=\frac{\tau_s^m}{r_s^{n+1}A'_s}W^m+O(W^{2m}).
\tag{1206.6}
$$
故 $f_T$ 在该点的极阶至多 $2m+1=p$。其最高项准确为
$$
a_sW^{-p},\qquad
a_s=-\frac{r_s^{2n+3}A'_sT(s)}{\tau_s^p}.
\tag{1206.7}
$$
若 $T(s)\ne0$，此系数非零，极阶就等于 $p$。

另一方面，(1206.3)、(1206.6) 给
$$
df_T=\frac{m\mathscr DT(s)}{\tau_sA'_s}W^{-2}dW
       +O(W^{m-2})dW.
$$
一个极阶至多 $p$ 的 Laurent 函数，其导数只有上述二阶极时，全部 $W^{-j}$、$2\le j\le p-1$ 的系数必为零。因此完整负主部为
$$
\boxed{\quad
f_T=a_sW^{-p}
-\frac{m\mathscr DT(s)}{\tau_sA'_s}W^{-1}+O(1).
\quad}
\tag{1206.8}
$$
这是原 $W$ 中的陈述。尤其 $d(a_sW^{-p})=0$ 没有授权将 $a_sW^{-p}$ 从有理函数、Frobenius 数据或节点过渡中抹掉。

### 3.2. 三个 CM 端点与无穷远

在 $b^3=1$，$A$ 为单位，$(T/A)'$ 正则。由于
$\gcd(m,n+1)=1$，原归一化曲线上
$$
\operatorname{ord}(r)=m,\qquad
\operatorname{ord}(u)=n+1.
$$
从而
$$
\operatorname{ord}(f_T)\ge m-(n+1)=2n+1>0.
\tag{1206.9}
$$
所以在三个原 CM 端点，$f_T$ 正则且消失。这并未说原半稳定图上这些支持尾的全部有限 log 列消失。

又 $\deg A=m-1$、$\deg h=2m$。原无穷远上 $u/b^2$ 为单位，$T/A=O(b^{-1})$，因此
$$
f_T=O(b^{-1}).
\tag{1206.10}
$$
所有无穷远点亦正则消失。除了 $A=0$、$r=0$、无穷远以外，式 (1206.2) 的全部分母均为单位；由此给出完整的极点清单。

### 3.3. 原 deck 角色

原实际作用为 $\delta^*b=\zeta^2b$、$\delta^*u=\zeta u$，见 R1193 (1193.1) 和 R1204 §1。$T/A$ 的角色是 $\zeta^2$，其 $b$ 导数角色为一，$r$ 不变。因此
$$
\delta^*f_T=\zeta^2f_T.
\tag{1206.11}
$$
这与原负 deck 返回一致，不以协变晶体的逆作用代替自然曲线拉回。

## 4. 接回原纯尖点目标时的边界

R1205 已付同一原纯尖点格的底空间恰为 $\ker\mathfrak c=\operatorname{im}C$。式 (1206.4) 因而为该底空间的每个实际 high-PS 返回提供了准确原函数，并给出其全部 SS、CM 和无穷远行为。

但 R1196 的 $\mathcal V_m$ 是同一原点差经过全部有限 Čech log、三个支持尾、节点反馈和全图 Serre 配对后的读数。原曲线分量上一形式 exact 不等于这整个图上的 de Rham 类为零。尤其 (1206.8) 的 $p$ 阶主部在微分后不可见，而在原 Frobenius/Čech 过渡中仍须逐项追踪。

本篇没有据此宣布 $\mathcal V_m|_{\ker\mathfrak c}$ 为零或非零，没有将 CM 端点的函数值零替代全部 CM normal 列，也没有将 R1208 更正后的 packet 单位传给指定 $C$ 或完整 MW 消去空间。后续计算使用 (1206.3) 的实际原函数降低同源配对，而必须保留 (1206.8) 的全部主部与原支持尾。

## 来源与核验

- [R1193](R1193-original-highest-primitive-packet-and-simple-Cauchy-CM-jet.md)：同一 Igusa 函数域、自然 deck 与中心微分。
- [R1200](R1200-original-canonical-Igusa-Weil-phase-and-rational-packet-pairing.md)：原 $\tau_s$、$\gamma$ 和 SS 参数规范。
- [R1201](R1201-original-highest-packet-kernel-log-unit.md)：原 Jacobi 方程与 SS 单位；完整 packet 单位按 R1208 的 node 更正读取。
- [R1204](R1204-original-PS-return-Cartier-kernel-and-cuspidal-quotient.md)：实际 PS 返回 $-3\gamma^2\mathscr DT$ 及其 Cartier 核。
- [R1205](R1205-original-cuspidal-deck-multiplicity-and-Cartier-kernel.md)：原纯尖点的准确底空间。
- R1196、R1197、R1199：原完整有限 log、CM 旗标和全图配对的范围。

root 直接展开证明，global_route 独立核准 (1206.3)；全部为纸面推导，未运行数学程序，未扩大任何有限扫描。主目标仍开放。
