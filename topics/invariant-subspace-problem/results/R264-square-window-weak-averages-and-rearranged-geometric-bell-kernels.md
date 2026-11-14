# R264：平方规模的弱高位平均与重排不变的几何、伸缩指数 Bell 分支排核

日期：2026-11-13（UTC）。作者：kernel。

状态：已证明的中间结论；root及boundary已全文核验。新点是以 $q\asymp r^2$ 的真实全 Haar 弱近单位替代强近单位，并将其非零标量弱极限与四次局部交换子预算配对。该改动覆盖 R260 尚未处理的一批 little-weak-ℓ¹ 行；不是只缩小一个无关紧要的常数。

## 1. 主结论

取
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad a_*\in\mathbb C.
$$
记 $\rho_n$ 为非零幅度 $|a_j|$ 的非增重排。
假设存在固定 $c,C,\beta>0$、$n_0$ 及 $0<\alpha\le1$，使
$$
\boxed{
c e^{-\beta n^\alpha}\le\rho_n\le C e^{-\beta n^\alpha}
\qquad(n\ge n_0).
}
\tag{1.1}
$$
$\alpha=1$ 为双侧几何尾，$0<\alpha<1$ 为双侧伸缩指数尾。
系数相位与物理排列完全任意；有限个低幅度排序位不受限制。
该假设保证 $a\in\ell^1$，且非零项无限多个。

取任意复 first 指数
$$
w=c_*+\sum_jb_j\chi_j,\qquad b\in\ell^2.
$$
令
$$
c_j=e^{-2b_j},\quad
R_j=V(c_jN_j),\quad V(z)=(I-z)(I+z)^{-1},
$$
$$
X_b=a_*I+\sum_ja_jR_j\in\mathcal A,
$$
$$
K_\nu=\sum_j a_j^\nu L_\nu(R_j)\in\mathcal A,\qquad
L_\nu(v)=
\left.\frac{d^\nu}{dt^\nu}
\log(\cosh t+v\sinh t)\right|_{t=0},
\quad \nu\ge2.
\tag{1.2}
$$
这些都是实际算子范数收敛的有界和；$X_b$ 等于 R176 的倾斜闭 first。
各 $K_\nu$ 字符为零。

**定理。** 对任意固定 $d\ge2$ 及原点邻域上的任意固定多变量解析芽 $\Phi$，
$$
\boxed{
\ker\bigl(X_b-\Phi(K_2,\ldots,K_d)\bigr)=\{0\}.
}
\tag{1.3}
$$
从而，对任意非零简单根多项式 $q$，
$$
\boxed{q(u)e^w\text{ 对原实际 }A\text{ 循环}.}
\tag{1.4}
$$
非零常数同样包括在内。

本稿不要求原物理顺序中的幅度满足 (1.1)，只要求幅度多重集满足。
所有选择最终都落实为有限个原物理位，且不改变原 $a_*$、$X_b$ 或 $A$。

## 2. 平方规模平均的真实全空间弱极限

先独立证明新的平均引理。
设 $r\to\infty$，$q_r$ 是整数，满足
$$
q_r/r^2\longrightarrow\kappa\in(0,\infty).
$$
令 $I_r$ 是任意恰有 $q_r$ 个物理位的集合，且 $\min I_r\to\infty$。
定义
$$
C_{I_r}=\frac2{q_r}\sum_{j\in I_r}E_j.
$$
则
$$
\boxed{
C_{I_r}^{\,r}\xrightarrow{\rm WOT}
\theta_\kappa I,\qquad
\theta_\kappa=e^{-1/(2\kappa)}>0,
\qquad
\sup_r\|C_{I_r}^{\,r}\|<\infty.
}
\tag{2.1}
$$

证明范数界：在这 $q=q_r$ 个独立计算位的 $s$ 孔层，
$\sum E_j$ 的范数平方至多
$$
(s+1)(q-s)\le(q+1)^2/4.
$$
各层的像正交，故
$$
\|C_{I_r}\|\le1+1/q,\qquad
\|C_{I_r}^{\,r}\|\le(1+1/q)^r\le e^{r/q}\longrightarrow1.
\tag{2.2}
$$

若 $f,g$ 为固定有限柱，充分大 $r$ 时其支撑低于 $\min I_r$。
每个高位处于真实 Haar 参考向量
$\Omega_+=(e_0+e_1)/\sqrt2$，且
$\langle E_j\Omega_+,\Omega_+\rangle=1/2$。
因为不同 $E_j$ 交换且平方为零，
$$
C_{I_r}^{\,r}
=(2/q)^r r!\sum_{\substack{F\subset I_r\\|F|=r}}
 \prod_{j\in F}E_j.
$$
所以准确有
$$
\boxed{
\langle C_{I_r}^{\,r}f,g\rangle
=\frac{(q)_r}{q^r}\langle f,g\rangle,\qquad
(q)_r=q(q-1)\cdots(q-r+1).
}
\tag{2.3}
$$
又
$$
\log\frac{(q)_r}{q^r}
=\sum_{j=0}^{r-1}\log(1-j/q)
=-\frac{r(r-1)}{2q}+O(r^3/q^2)
\longrightarrow-\frac1{2\kappa}.
$$
结合 (2.2)、有限柱稠密性，就得到整个原 Haar 空间上的 WOT 极限 (2.1)。

这里不宣称强收敛于恒等。
后面的最高交换子配对只测试固定的 $Df$ 与 $Cg$，
所以非零标量 WOT 极限已经足够。

## 3. 有界倾斜分支及任意跨度的 carry 界

固定 $a,b,d,\Phi$，置
$$
Y=\Phi(K_2,\ldots,K_d),\qquad T=X_b-Y,\qquad M=\ker T.
$$
由于 $a\in\ell^1$，$X_b,Y,T\in\mathcal A\subset B(H)$。
所以本稿所有自然幂的完整域都是 $H$；它们不是未经核对的形式幂。
$T$ 是实际有界 $C$ 对称算子。

有固定常数
$$
0<c_-\le|c_j|\le c_+<\infty,\qquad
\sup_j\|(I\pm c_jN_j)^{-1}\|<\infty,
$$
$$
\sup_j\|V(\pm c_jN_j)\|<\infty.
\tag{3.1}
$$
大 $j$ 用 $c_j\to1$ 和
$N_j^2=\eta_jN_{j+1}$ 得统一逆界；有限低位分别由准幂零性取界。
所有常数可依赖固定行和固定解析芽，不依赖 $r$ 或所选位。

设 $F$ 是任意有限位集，$\min F\ge h$。
置
$$
J_F=\prod_{j\in F}M_{\chi_j},\qquad
\gamma_F(Q)=J_FQJ_F,\qquad s_j=-1\ (j\in F),\ s_j=1\ (j\notin F).
$$
真实有限链及物理反射给
$$
\|\gamma_F(N_j)-s_jN_j\|\le
\begin{cases}
2\alpha_h/\alpha_j,&j<h,\\
2\eta_j,&j\ge h.
\end{cases}
\tag{3.2}
$$
第二行逐位使用
$N_j=E_j+\eta_jE_j^*N_{j+1}$；它与 $\max F$ 无关。
(3.1) 的逆差公式将此传给 $V(c_jN_j)$，
固定多项式幂差将其传给每个 $L_\nu$。

定义
$$
\widehat X_F=X_b+\sum_{j\in F}a_j
 \bigl(V(-c_jN_j)-R_j\bigr),
$$
$$
\widehat K_{\nu,F}
=K_\nu+\sum_{j\in F}a_j^\nu
 \bigl(L_\nu(V(-c_jN_j))-L_\nu(R_j)\bigr),
\quad
\widehat Y_F=\Phi(\widehat K_{2,F},\ldots,\widehat K_{d,F}),
$$
$$
A_F=(\widehat X_F-\widehat Y_F)-T,\qquad
E_F=\gamma_F(T)-(\widehat X_F-\widehat Y_F).
\tag{3.3}
$$
$A_F\in\mathcal A$ 与 $T$ 交换。

若 $\sum_{j\in F}|a_j|^2\to0$，
则 $\widehat{\mathbf K}_F$ 一致接近原元组。
固定小多圆周上的 Neumann 逆差及逐因子 Cauchy 差，
给 $\widehat Y_F$ 与 $Y$ 的统一 Lipschitz 界。
$\gamma_F(\mathbf K)$ 的预解式范数与原元组相同；
两个元组之间不需要互相交换，只在固定次序的预解式乘积中逐因子相减。

对 (3.2) 加权求和，用
$$
\sum_{j<h}|a_j|^\nu\frac{\alpha_h}{\alpha_j}
\le C_\nu\eta_{h-1},\qquad
\sum_{j\ge h}|a_j|^\nu\eta_j
\le C_\nu'\bar\eta_h,\qquad
\bar\eta_j=e^{-770\,16^j},
$$
得到
$$
\boxed{\|E_F\|\le C_E\bar\eta_{h-1}.}
\tag{3.4}
$$
常数不依赖 $|F|$ 或 $\max F$。
由于本稿的 $T$ 全空间有界，直接有
$$
\|\operatorname{ad}_T^sE_F\|
\le (2\|T\|)^s\|E_F\|.
\tag{3.5}
$$
因此任意物理跨度不再带来一个随最大位置增长的头成本。

## 4. 从幅度排序窗口选出高物理位

下面先处理 $\alpha=1$。
令
$$
\gamma=\frac1{4\beta},\qquad
\kappa=\frac1{8\beta},
$$
$$
k_r=\lceil\gamma r^3\rceil,\qquad
q_r=\lceil\kappa r^2\rceil,\qquad
h_r=\lceil3\log_2r\rceil.
\tag{4.1}
$$
$k_r$ 是幅度排序秩，$h_r$ 是物理位置截断，两者不同。

取幅度排序中秩属于
$$
\{k_r,\ldots,k_r+q_r+h_r-1\}
$$
的 $q_r+h_r$ 个实际指标。
删除物理位置 $j<h_r$ 的项至多删除 $h_r$ 项，
所以剩余至少 $q_r$ 项。
任选恰有 $q_r$ 项的集合 $I_r$。
于是
$$
\boxed{
\min I_r\ge h_r,\qquad
\ell_r\le|a_j|\le A_r\quad(j\in I_r),
}
\tag{4.2}
$$
其中可取
$$
A_r=C e^{-\beta k_r},\qquad
\ell_r=c e^{-\beta(k_r+q_r+h_r)}.
\tag{4.3}
$$
不要求这些物理指标相邻，不控制其最大值。

由 (4.1)，
$$
\beta r(k_r+q_r+h_r)
=\frac14r^4+\frac18r^3+O(r\log r),
\tag{4.4}
$$
$$
-\beta k_r+\beta r(q_r+h_r)
=-\frac18r^3+O(r\log r).
\tag{4.5}
$$
同时
$$
\boxed{
\bar\eta_{h_r-1}
\le \exp\left[-\frac{770}{16}r^{12}\right].
}
\tag{4.6}
$$
因此物理位只需增长到 $O(\log r)$，实际 carry 就已远小于随后四次输入成本。
排序窗口中的幅度则决定第一阶与 Bell 误差的相对大小。

## 5. 高位输入、真实主项及完整误差

简写 $q=q_r$、$h=h_r$。
对 $F\subset I_r$、$|F|=r$，令
$$
p_F=\prod_{j\in F}a_jc_j,\qquad
\mathcal B_r=\frac1{(-2q)^r}\sum_{|F|=r}p_F^{-1}J_F.
\tag{5.1}
$$
其绝对系数和为
$$
S_r\le\frac{(2c_-\ell_r)^{-r}}{r!}.
$$
由 (4.4)，
$$
\boxed{
\|\mathcal B_r\|\le S_r
\le\frac{\exp[\frac14r^4+\frac18r^3+O(r\log r)]}{r!}.
}
\tag{5.2}
$$
这是与四次局部交换子配对的准确输入成本。

由
$$
V(-cN)-V(cN)=4cN(I-c^2N^2)^{-1}
$$
及固定多变量 Cauchy 差，令
$$
P_F=4\sum_{j\in F}a_jc_jN_j,
$$
得到
$$
\boxed{
\|P_F\|\le C_PrA_r,\quad
\|A_F-P_F\|\le C_ArA_r^2,\quad
\|A_F\|\le C_0rA_r.
}
\tag{5.3}
$$
第一阶有理余项至多 $CrA_r\bar\eta_h$；
(4.3)、(4.6) 使 $\bar\eta_h\le A_r$ 对充分大 $r$ 成立。
所选 Bell 改变量至多固定常数乘 $rA_r^2\to0$，
所以 §3 的统一轮廓确实可用。

对 $f\in M$，$v=J_Ff$ 满足
$$
Tv=-(A_F+E_F)v.
$$
使用有界递归
$$
Q_0=I,\qquad Q_{n+1}=[T,Q_n]-Q_n(A_F+E_F)
$$
及 $[T,A_F]=0$。
与 R236 相同的自含权计数给
$$
\boxed{
\|T^rJ_Ff-(-A_F)^rJ_Ff\|
\le(r+1)!C_E\bar\eta_{h-1}
 (1+\|A_F\|+2\|T\|)^r\|f\|.
}
\tag{5.4}
$$
所有算子有界，故每次幂和配对均在完整 $H$ 上。

### 5.1 非交换误差

(5.4) 乘 $S_r$ 后，上界为
$$
\bar\eta_{h-1}
 \exp\left[\frac14r^4+O(r^3+r\log r)\right]\|f\|
\longrightarrow0
\tag{5.5}
$$
，由 (4.6) 直接得到。

### 5.2 Bell 替换误差

真实幂差给
$$
\|A_F^r-P_F^r\|
\le C_Ar^2(C_0r)^{r-1}A_r^{r+1}.
$$
乘 $S_r$，并用 $r!\ge(r/e)^r$，完整误差至多
$$
C_1rA_r(C_2A_r/\ell_r)^r\|f\|.
$$
其对数由 (4.3)、(4.5) 控制为
$$
\boxed{
-\frac18r^3+O(r\log r)\longrightarrow-\infty.
}
\tag{5.6}
$$
这一步支付了幅度窗口中非可比的几何幅度损失；
没有把 $A_r/\ell_r=e^{O(r^2)}$ 当作固定常数。

### 5.3 重复位与实际 carry

所有 $N_j$ 交换。不同指标的项恰为
$$
4^rr!p_F\prod_{j\in F}N_j.
$$
其余项含 $N_j^2=\eta_jN_{j+1}$，所以
$$
\left\|P_F^r-4^rr!p_F\prod_{j\in F}N_j\right\|
\le\bar\eta_h(C_PrA_r)^r.
$$
乘 $S_r$ 后误差至多
$$
\bar\eta_h(C_3A_r/\ell_r)^r\|f\|\longrightarrow0,
$$
因为其正对数仅为 $O(r^3+r\log r)$，而 (4.6) 给十二次负阶。

物理 $E_jJ_j=E_j$，故
$$
\left\|\left(\prod_{j\in F}N_j\right)J_F-\prod_{j\in F}E_j\right\|
\le r\bar\eta_h.
$$
主项总系数绝对值不超过 $2^r$，最后误差至多
$2^rr\bar\eta_h\|f\|\to0$。

因此
$$
\boxed{
\|T^r\mathcal B_rf-C_{I_r}^{\,r}f\|
\le\epsilon_r\|f\|,\qquad \epsilon_r\to0,\quad f\in M.
}
\tag{5.7}
$$
全部 $a_j$ 与 $c_j$ 的复相位在 $p_F$ 中准确抵消。

## 6. 输出的非零弱极限

由 §2 及 $q_r/r^2\to\kappa=1/(8\beta)$，
$$
C_{I_r}^{\,r}\xrightarrow{\rm WOT}e^{-4\beta}I.
$$
结合 (5.7)，得到
$$
\boxed{
T^r\mathcal B_rf\rightharpoonup e^{-4\beta}f
\qquad(f\in M),
}
\tag{6.1}
$$
且这些输出在 $M\to H$ 的算子范数上一致有界。

$e^{-4\beta}$ 对固定 $\beta$ 是严格正的固定常数；
后面只需将最终配对等式除以它。
没有声称这些输出强趋于 $f$，也没有要求未知 $f$ 的任何尾速率。

## 7. 固定局部矩阵的准确四次交换子

固定局部矩阵 $D$，支撑位低于 $H$。
令
$$
K_{\nu,\ge H}=\sum_{j\ge H}a_j^\nu L_\nu(R_j),\qquad
Y_{\ge H}=\Phi(K_{2,\ge H},\ldots,K_{d,\ge H}),
$$
$$
Z_H=a_*I+\sum_{j\ge H}a_jR_j+
 \left(\sum_{j<H}a_j\right)I-Y_{\ge H},
$$
$$
G_H=\sum_{j<H}a_j(R_j-I)-(Y-Y_{\ge H}),
\qquad T=Z_H+G_H.
$$
这些算子全有界；$D$ 与尾算子 $Z_H$ 交换，$G_H$ 也与 $Z_H$ 交换。

有限低位的准确式
$$
R_j-I=-2c_jN_j(I+c_jN_j)^{-1}
=A\left(-2c_jd_j^{-1}A^{2^j-1}(I+c_jN_j)^{-1}\right)
$$
及 $L_\nu(1)=0$ 给
$$
K_\nu-K_{\nu,\ge H}=A U_{\nu,H},\qquad U_{\nu,H}\in\mathcal A.
$$
多变量预解式逐坐标相减后，$Y-Y_{\ge H}$ 也有明确有界 $A$ 因子。
所以
$$
\boxed{G_H=A U_H,\qquad U_H\in\mathcal A.}
\tag{7.1}
$$
这里只有固定有限低头差被有界除以 $A$。

因此
$$
\operatorname{ad}_T^rD=\operatorname{ad}_{G_H}^rD.
$$
由原权的 R109 界
$$
\|A^n\|\le
\exp\left[-\frac{100}{15}n^4+105n^3\right]
$$
和有界交换子展开，得到
$$
\boxed{
\|\operatorname{ad}_T^rD\|
\le\|D\|(2\|U_H\|)^r
 \exp\left[-\frac56r^4+105r^3\right].
}
\tag{7.2}
$$
$U_H$ 只依赖固定局部测试 $D$ 的头界，不随 $r$ 增长。

## 8. 弱配对已足以排核

记 $\mathcal B(x,y)=\langle x,Cy\rangle$。
因为 $T\in\mathcal A$ 是有界 $C$ 对称，对 $f,g\in M$，
有界 Leibniz 展开和 $Tg=0$ 给
$$
\mathcal B(DT^r\mathcal B_rf,g)
=(-1)^r\mathcal B((\operatorname{ad}_T^rD)\mathcal B_rf,g).
\tag{8.1}
$$
由 (5.2)、(7.2)，右端绝对值至多固定常数乘
$$
\frac1{r!}
\exp\left[
-\frac7{12}r^4+
\left(105+\frac18\right)r^3+O(r\log r)
\right]\|f\|\,\|g\|
\longrightarrow0.
\tag{8.2}
$$
而 (6.1) 与固定有界 $D$ 给左端极限
$$
e^{-4\beta}\mathcal B(Df,g).
$$
故
$$
\mathcal B(Df,g)=0
\quad(f,g\in M,\ D\text{ 任意固定有限局部矩阵}).
\tag{8.3}
$$

原 Haar 局部全矩阵代数不可约，其每个非零向量的局部轨道线性张成稠密。
若 $f=g\ne0$ 属于 $M$，(8.3) 迫 $Cf$ 正交于该稠密轨道，矛盾。
所以 $M=0$，完成几何幅度情形的 (1.3)。

该论证只需 WOT 极限；把输入归一化要求提高为 SOT 近单位会丢失本稿覆盖的临界四次成本窗口。

## 9. 全部 0<alpha<1 的伸缩指数幅度

现设 (1.1) 中 $0<\alpha<1$。
选取任意固定实数 $\nu$ 满足
$$
\max(1,3\alpha)<\nu<3.
\tag{9.1}
$$
令
$$
k_r=\left\lceil(r^\nu/\beta)^{1/\alpha}\right\rceil,\qquad
q_r=r^2,\qquad h_r=\lceil3\log_2r\rceil.
\tag{9.2}
$$
仍从幅度排序窗口 $[k_r,k_r+q_r+h_r)$ 删除物理前 $h_r$ 位，
选出 $q_r$ 个实际位。
此时
$$
A_r=C e^{-\beta k_r^\alpha},\qquad
\ell_r=c e^{-\beta(k_r+q_r+h_r)^\alpha}
$$
给同样的真实幅度上下界，且 $\min I_r\ge h_r$。

由 (9.1)，
$$
k_r/r^3\longrightarrow\infty,\qquad
\beta k_r^\alpha=r^\nu+o(1).
\tag{9.3}
$$
因为 $x^\alpha$ 凹，
$$
0\le(k_r+q_r+h_r)^\alpha-k_r^\alpha
\le\alpha(q_r+h_r)k_r^{\alpha-1}.
$$
因此
$$
r\beta\bigl((k_r+q_r+h_r)^\alpha-k_r^\alpha\bigr)
\le
\frac{\alpha r(q_r+h_r)}{k_r}\,
 \beta k_r^\alpha
=o(r^\nu).
\tag{9.4}
$$

现在全部关键预算变为：

- 输入：
  $$
  \log(S_r r!)
  \le r\beta(k_r+q_r+h_r)^\alpha+O(r)
  =r^{\nu+1}+o(r^{\nu+1})=o(r^4).
  $$
- Bell 替换误差：
  $$
  \log\bigl(CrA_r(C'A_r/\ell_r)^r\bigr)
  \le-r^\nu+o(r^\nu)+O(r)\longrightarrow-\infty,
  $$
  因 $\nu>1$。
- 所有非交换及实际 carry 误差仍被 (4.6) 的
  $e^{-c r^{12}}$ 吸收；重复位的额外正对数也至多 $o(r^\nu)+O(r)$。
- $q_r/r^2=1$，故真实全空间弱主项为
  $C_{I_r}^{\,r}\to e^{-1/2}I$，标量严格非零。
- 局部交换子仍为 (7.2)，与 $o(r^4)$ 输入相乘后趋零。

所以 §§5–8 的完整论证逐项成立，得到所有 $0<\alpha<1$ 的 (1.3)。
这一步只改变已经明确列出的标量预算，所有算子、逆和配对仍是同一个原 Haar 模型中的真实对象。

## 10. 简单根点态多项式及指数权

R176 的准确加权 Bell 实现给
$$
q(u)e^w=P_{q,b}(X_b)e^w.
$$
这里 $X_b$ 有界，$P_{q,b}(X_b)\in\mathcal A$ 全域有界；
$e^w$ 是已证循环向量，故其多项式轨道也是这个有界算子的图核心。

若 $q$ 的根均简单，在原点附近对有限 Bell 参数
$(K_2,\ldots,K_d)$ 使用全纯隐函数定理，
得到实际标量解析分支 $\Phi_1,\ldots,\Phi_d$，并有
$$
P_{q,b}(X_b)
=q_d\prod_{\mu=1}^d
 \bigl(X_b-\Phi_\mu(K_2,\ldots,K_d)\bigr).
$$
所有因子属于 $\mathcal A$，彼此交换。
(1.3) 使每个因子单射，所以乘积单射。
它的 $C$ 对称性给稠密像，图循环判据遂得
$q(u)e^w$ 循环，即 (1.4)。

一次多项式使用常数芽；非零常数使用 $e^w$ 的循环性。
一般重复根仍不能由解析分支或简单根极限无证补齐。

## 11. 范围及剩余问题

(1.1) 的行全属于 little-weak-ℓ¹，且 first 系数绝对可和。
因而本稿确实推进 R260 剩余的同字符分支，
不是重复非 little-weak-ℓ¹ 排核。

结论依赖幅度多重集，因此允许任意物理重排和任意复相位。
删除前 $h_r$ 个物理位只付 $O(\log r)$ 个排序秩，
这个准确有限损失已列入所有几何与伸缩指数预算。

本稿没有覆盖超几何幅度 $e^{-\beta n^\alpha}$、$\alpha>1$，
也没有覆盖全部 little-weak-ℓ¹ 行或一般重复根多项式。
没有把全空间核排除当成任意不变限制上的稠密像，
没有把边界核转成 Haar 正常核。
普通 Hilbert 不变子空间问题仍未完成。

## 已用接口

- R176：复倾斜、实际 Bell 累积量与加权图循环判据。
- R236：高位反射的实际主项、最高局部交换子配对。
- R259：多变量 Cauchy 差及有限低头的明确有界 A 因子。
- R109：原 A 幂的四次范数预算。
- 本稿 §2 独立证明新的全 H 弱平均，§4 与 §9 独立支付其增长参数。

同步当前 main：R236 的规范交替调和行全部重数已经另由 Hermite/Bézout 证明关闭；本文关于一般混合重根的保留不撤销该规范结论。
