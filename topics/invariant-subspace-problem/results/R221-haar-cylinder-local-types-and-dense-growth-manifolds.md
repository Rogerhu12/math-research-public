# R221：Haar 有限柱向量的局部增长型与稠密但不闭的增长流形

日期：2026-11-13（UTC+8）。作者：root。状态：完整证明；已由 normal_states 独立逐式复核。

本文在原 Haar 表示内计算向量范数，不能用负整数边界中的真空替代它。全部结果是普通 ISP 的中间结论；末节特别证明相应慢增长线性流形的闭包仍是整个空间。

## 1. 模型、输入与结论

令 $H=L^2(\mathbb Z_2,\mu)$，每个物理二位因子的参考向量为 $\Omega_+=(e_0+e_1)/\sqrt2$。逐位任选 $X_j\in\{N_j,Y_j\}$，取正系数
$$
a_j=(j+1)^{-2},\qquad S=\sum_{j\ge0}a_jX_j.
$$
包含两种固定模型 $S_N,S_Y$，也允许逐位混选。这里没有任意系数相位的结论。

已证明的真实估计为
$$
N_j=E_j+\eta_jE_j^*N_{j+1},\quad
\eta_j\le e^{-77016^j},\quad E_j=e_{10}^{(j)},
$$
以及 R215 的单因子及全空间估计。令 $X_j^{[k]}$ 为在第 $k$ 位截断 carry 的实际有限头，置
$$
H_k=\sum_{j<k}a_jX_j^{[k]},\quad
D_k=\sum_{j\ge k}a_jE_j,\quad
\widehat S_k=H_k+D_k.
$$
R215 和同轮全方向增长证明给
$$
\|S-\widehat S_k\|\le26\eta_{k-1},\quad
\|S\|\le6,\quad\|\widehat S_k\|\le8,
\tag{1.1}
$$
$$
\|e^{zS}\|,\|e^{z\widehat S_k}\|\le e^{16\sqrt{|z|}},
\quad
\|R(\lambda,S)\|,\|R(\lambda,\widehat S_k)\|
\le2|\lambda|^{-1}e^{128/|\lambda|}.
\tag{1.2}
$$
这里 $R(\lambda,T)=(\lambda I-T)^{-1}$，所有复 $\lambda\ne0$ 均包括。

定义
$$
\gamma(\theta)=\frac\pi2\sqrt{\sqrt2+\cos\theta},\qquad
\kappa(\theta)=\frac{\gamma(\theta)^2}{4}
=\frac{\pi^2}{16}(\sqrt2+\cos\theta).
\tag{1.3}
$$

**定理1.1。** 若 $0\ne f\in H$ 是固定有限柱向量，则一致于 $\theta\in\mathbb R$，
$$
\boxed{
\log\frac{\|e^{r e^{i\theta}S}f\|}{\|f\|}
=\gamma(\theta)\sqrt r+O_f(\log^2(r+2)).
}
\tag{1.4}
$$
其局部预解式满足全部方向的上界
$$
\boxed{
\log\frac{s\|R(s e^{i\theta},S)f\|}{\|f\|}
\le\frac{\kappa(\theta)}s+O_f(\log^2(2+s^{-1})),
\quad s\downarrow0,
}
\tag{1.5}
$$
且沿正实轴有相同常数的上下界：
$$
\boxed{
\log\frac{s\|R(s,S)f\|}{\|f\|}
=\frac{\kappa(0)}s+O_f(\log^2(2+s^{-1})).
}
\tag{1.6}
$$
全部大 $O$ 常数可以与 $N/Y$ 的选择无关。对于 (1.4)—(1.5)，只需依赖一个容纳 $f$ 的有限头长度；(1.6) 的下界另允许依赖 $f$ 的一个非零物理坐标。

## 2. 纯尾对 Haar 真空的准确乘积

一位直接计算给
$$
\|(I+wE)\Omega_+\|^2
=\frac{1+|1+w|^2}{2}
=1+\operatorname{Re}w+\frac{|w|^2}{2}.
$$
因此，由有限张量乘积再取算子范数极限，
$$
\log\|e^{r e^{i\theta}D_k}\Omega_{\ge k}\|
=\frac12\sum_{j\ge k}
\log\left(1+\frac{r\cos\theta}{(j+1)^2}
+\frac{r^2}{2(j+1)^4}\right).
\tag{2.1}
$$
这个等式就在原 Haar 不完全张量积中成立。

置 $c=\cos\theta$。函数
$$
F_{r,c}(x)=\frac12\log(1+cr/x^2+r^2/(2x^4))
$$
满足一致积分比较
$$
\sum_{n\ge1}F_{r,c}(n)
=\int_0^\infty F_{r,c}(x)\,dx+O(\log(r+2)),
\quad -1\le c\le1.
\tag{2.2}
$$
证明如下。写 $t=r/x^2$，则
$$
\tfrac12\le1+ct+t^2/2\le(1+t)^2.
$$
故 $\int_0^1|F_{r,c}(x)|dx\le\log(1+r)+2+\tfrac12\log2$。
在 $x\ge1$ 上，$F$ 的导数最多改变一次符号（其符号由 $c+t$ 决定），函数下界为 $-\tfrac12\log2$，在无穷处趋于0。总变差至多 $\log(1+r)+\log2$。
逐个单位区间用微积分基本定理比较 $F(n)$ 与其积分，误差不超过该总变差。这证明 (2.2)，也处理 $c<0$ 时函数不是单调的问题。

取
$$
b=\frac{c+i\sqrt{2-c^2}}2,
\quad |b|=2^{-1/2},\quad \operatorname{Im}b>0.
$$
则 $1+c/x^2+1/(2x^4)=(1+b/x^2)(1+\bar b/x^2)$。主支平方根实部为正。由分部积分（或从正实 $b$ 对割平面作解析延拓），
$$
\int_0^\infty\log(1+b/x^2)dx=\pi\sqrt b.
$$
端点均为0；导数后的积分 $\int_0^\infty (x^2+b)^{-1}dx=\pi/(2\sqrt b)$，在该割平面上的紧集有积分支配，保证所述解析延拓合法。因此
$$
\frac12\int_0^\infty\log(1+c/x^2+1/(2x^4))dx
=\pi\operatorname{Re}\sqrt b
=\frac\pi2\sqrt{\sqrt2+c}.
\tag{2.3}
$$
变量代换 $x=\sqrt r\,u$ 后，由 (2.2)—(2.3) 得整个纯和的主项 $\gamma(\theta)\sqrt r$。删去前 $k$ 个因子的对数成本至多
$$
k\bigl(\log(1+r)+\tfrac12\log2\bigr).
\tag{2.4}
$$

## 3. 真实有限头与任意固定有限柱

设 $f$ 只依赖低 $h$ 位，$\|f\|=1$。给定大 $r$，取
$$
k=1+\lceil\log_{16}(r+1)\rceil,
$$
并要求 $r$ 足够大使 $k\ge h$。写
$$
f=f_{<k}\otimes\Omega_{\ge k},\qquad\|f_{<k}\|=1.
$$
头尾分离准确给
$$
\|e^{z\widehat S_k}f\|
=\|e^{zH_k}f_{<k}\|\,
\|e^{zD_k}\Omega_{\ge k}\|.
\tag{3.1}
$$
R215 单因子估计对 $z$ 和 $-z$ 同时适用，全部头算子交换，故
$$
\log\|e^{\pm zH_k}\|
\le k\log(2(1+3r))+2(\log_+(3r))^{4/3}
=O(\log^2(r+2)).
$$
用 $e^{-zH_k}$ 作实际有界逆，得到
$$
e^{-C\log^2(r+2)}\le\|e^{zH_k}f_{<k}\|
\le e^{C\log^2(r+2)}.
\tag{3.2}
$$
因此 (2.1)—(2.4)、(3.1)—(3.2) 已给混合模型的 (1.4)。

Duhamel 恒等式及 (1.1) 给真实误差
$$
\|e^{zS}-e^{z\widehat S_k}\|
\le26r e^{8r-770(r+1)}\le e^{-700r}.
\tag{3.3}
$$
同时 $\min_\theta\gamma(\theta)=\frac\pi2\sqrt{\sqrt2-1}>0$，所以模型向量范数最终趋于无穷，减去 (3.3) 不改变其对数的 $O(\log^2r)$ 误差。这证明 (1.4)。

## 4. 局部预解上界

取 $s=q^{-1}$、$\lambda=q^{-1}e^{i\theta}$。旋转 Laplace 积分在整个 Hilbert 空间中按范数收敛，故
$$
\|R(\lambda,S)f\|
\le\int_0^\infty e^{-t/q}\|e^{t e^{-i\theta}S}f\|dt.
$$
因为 $\gamma(-\theta)=\gamma(\theta)$，(1.4) 及有界时间段给
$$
\|R(\lambda,S)f\|/\|f\|
\le\int_0^\infty
\exp(-t/q+\gamma(\theta)\sqrt t+B_h\log^2(t+2))dt.
\tag{4.1}
$$
将 $\sqrt t=qv$ 代入，使用
$$
B_h\log^2(2+q^2v^2)\le8B_h\log^2(q+2)+8B_hv^2,
$$
并对 $-(q-8B_h)v^2+\gamma(\theta)qv$ 配方。
其最大值为
$$
\frac{\gamma(\theta)^2q^2}{4(q-8B_h)}
=\kappa(\theta)q+O_h(1)
$$
一致于 $\theta$；余下高斯积分仅付 $O_h(\log q)$。于是得到 (1.5)。

## 5. 正实轴下界：用实际 Haar 行投影，不能偷换表示

令 $q=s^{-1}\to\infty$，现在取
$$
k=1+\lceil\log_{16}(q+1)\rceil\ge h.
$$
把 $f$ 在低 $h$ 位的物理计算基写为 $f=\sum_{n<2^h}f_n e_n$，令 $n_0$ 是最小的非零坐标。
在低 $k$ 位中，其 $n_0$ 坐标准确为
$$
d_k=2^{-(k-h)/2}f_{n_0}\ne0,
$$
而所有更小的物理整数坐标为0。

真实有限头 $H_k$ 是有限加权前移的无常数多项式：它只把整数指标增大。因此对每个整数 $\ell\ge1$，
$$
\langle H_k^\ell f_{<k},e_{n_0}\rangle=0.
$$
设 $\Pi_{n_0}$ 是低头第 $n_0$ 个物理坐标行（其余尾保留）。低头和纯尾交换、且低头严格三角，于是实际预解的有限三角展开准确给
$$
\boxed{\Pi_{n_0}R(s,\widehat S_k)f=d_k R(s,D_k)\Omega_{\ge k}.}
\tag{5.1}
$$
也可从范数收敛的预解 Neumann 级数逐项验证：每个含正次 $H_k$ 的项在此行消失。

$D_k$ 是原 Haar $L^2$ 上的正算子：$E_j=e_{10}^{(j)}$ 把第 $j$ 位的非负输入送到非负输出。其幂和预解也为正。对 $t\ge0$，逐项比较真实范数收敛级数给
$$
0\le e^{tD_k}\le s e^{st}R(s,D_k),
$$
因为 $t^n/n!\le e^{st}s^{-n}$。应用于正向量 $\Omega_{\ge k}=1$，利用 $L^2$ 正锥的范数单调性，得到
$$
\|R(s,D_k)\Omega_{\ge k}\|
\ge s^{-1}e^{-st}\|e^{tD_k}\Omega_{\ge k}\|.
\tag{5.2}
$$
在 (5.2) 中取 $t=\gamma(0)^2q^2/4$。由 §2 的准确乘积，删去前 $k=O(\log q)$ 个因子仅付 $O(\log^2q)$，故
$$
\log\bigl(q^{-1}\|R(s,D_k)\Omega_{\ge k}\|\bigr)
\ge\kappa(0)q-O(\log^2(q+2)).
\tag{5.3}
$$
由 (5.1)，前面的 $d_k$ 再付 $O_f(\log q)$。

最后，(1.1)—(1.2) 的实际逆差给
$$
\|R(s,S)-R(s,\widehat S_k)\|
\le104q^2e^{-514q-770}.
\tag{5.4}
$$
(5.3) 指数增长，故该差可吸收。这证明 (1.6) 的下界；上界是 (1.5) 在 $\theta=0$ 的特例。对 $S_Y$ 并未声称整个 $S_Y$ 为正：正性只用于已经分离的纯尾 $D_k$。

## 6. 严格的局部型差距

[R218](R218-exact-radial-semigroup-and-resolvent-types.md) 的精确全空间型为
$$
\mathsf C=\int_0^\infty\operatorname{arsinh}(1/(2x^2))dx
=\frac{\Gamma(1/4)^2}{2\sqrt{2\pi}},
\qquad\mathsf K=\mathsf C^2/4.
$$
有严格不等式
$$
\gamma(0)<\mathsf C,\qquad\kappa(0)<\mathsf K.
\tag{6.1}
$$
这里不依靠数值比较。对每个 $u>0$，$\Omega_+$ 不是 $(I+uE)^*(I+uE)$ 的最大特征向量（该矩阵在两坐标上的行和差为 $u^2$），所以
$$
\log\|(I+uE)\Omega_+\|<\log\|I+uE\|.
$$
两边取 $u=x^{-2}$ 后积分，即给 (6.1)。两积分均有限，差在任意有限正区间上严格正。

因此固定有限柱向量的正轴预解型严格低于全算子范数型；同时其半群主增长率确实依赖方向，而全空间算子范数的主增长率不依赖方向。

## 7. 增长流形稠密、真且不闭

固定任意
$$
\kappa(0)<\tau<\mathsf K.
$$
定义有界算子列
$$
L_n=n^{-1}e^{-\tau n}R(1/n,S),\qquad n\ge1,
$$
及线性流形
$$
\mathcal E_\tau=\{x\in H:\sup_{n\ge1}\|L_nx\|<\infty\}.
\tag{7.1}
$$
由 (1.6)，全部有限柱向量属于 $\mathcal E_\tau$，故它稠密。
由全空间精确型，
$$
\log\|L_n\|=(\mathsf K-\tau)n+O(\log^2(n+2))\longrightarrow\infty.
$$
一致有界原理给 $\mathcal E_\tau\ne H$。

更准确地，$F_m=\{x:\sup_n\|L_nx\|\le m\}$ 是闭集。如果任何 $F_m$ 含一个非空球，线性与三角不等式就给 $\sup_n\|L_n\|<\infty$，矛盾。因此每个 $F_m$ 内部为空，$\mathcal E_\tau=\bigcup_mF_m$ 为第一纲稠密线性流形，特别不闭。

它还保持于 $S$ 的整个交换子：若 $CS=SC$，则 $L_nC=CL_n$，故 $C\mathcal E_\tau\subseteq\mathcal E_\tau$。因为每个与 $A$ 交换的算子也与 $S$ 交换，这同样给 $A$ 的交换子不变性。但
$$
\overline{\mathcal E_\tau}=H,
$$
所以把该慢增长空间直接取闭包不会给普通不变子空间。

此处没有证明任意未知闭不变空间与 $\mathcal E_\tau$ 有非零交，也没有构造将整个 $H$ 送入 $\mathcal E_\tau$ 的非零有界交换正则器。后二者都不能由环境稠密性推出。
