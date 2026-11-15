# 原极端 carry 中乘后 forcing 的实际短行

日期：2026-11-15。**状态：下述完整目标恒等式已证明；指定向量在原全像中的归零仍未判定。**
本 note 保存 R712 工作线的一个具体计算，不将它登记为新的非零结论。
原来源、同一个因子整提升和同一个修正 $R$ 全部保持。

## 1. 同一来源与极端 carry

使用 R502/R552 的实际来源
$$
P^{\rm fact}=d^{-C_D}t^rQF^3\in\mathcal W_D,\qquad
d=1+8t,\quad p=6s-1>101,
$$
及其同一整 Hensel 支 $Y=\widetilde\psi(t)$。令
$$
e=(\mathcal EF)|_C,\qquad f_2=(\mathcal E^2F)|_C,\qquad
\eta=\log(g/\widetilde\psi)=t^hu+p\xi ,
$$
其中 $u(0)$ 和 $e(0)$ 为单位，$\xi\in\mathcal O[t]_{<h}$。
保同一个实际分支常数：$\xi_0=-\log\widetilde\psi(0)/p\bmod p$，不预设为零。
R507 的常数归一需要改变原因子提升；乘以本篇的非单位 $\mu$ 后，
若未另付来源返回，不能把该改动自动认作同一指定目标的无害变化。

这里只取 R502 的以下实际子窗：
$$
\boxed{\ell=r,\quad k=2h+r-s=r-1,\quad s=2h+1,\quad1\le r<h.}
\tag{1}
$$
原 $a=p\kappa$ 为 Gaussian 单位，
$$
b_s=(t/w(t))^s,\qquad
T=s-r=2h+1-r,\qquad q=T-h=h+1-r.
\tag{2}
$$
所以 $0<q\le h$、$h<T\le2h$。

令 $\mu$ 是已付 R697 或 R701 来源返回所用的同一个实际乘子。
本 note 只用其物理评价的准确性质
$$
\boxed{\mu_{\rm phys}=t\,m(t,Y_{\rm phys}),\qquad m(0,1)\in k^\times.}
\tag{3}
$$
它的两或三 charge 成本、十九角和无穷远门仍按对应原结果支付；
(3) 不是免费加入任意单位列。

## 2. 先在整个原目标相乘

R502 的全首 Bockstein 是
$$
\begin{aligned}
\beta_J(P^{\rm fact})={}&
\epsilon V_0\{b_st^{h+k}u^3+6at^{r+h}u\xi\}
+3a\epsilon^2V_0b_st^ku^2\\
&+\epsilon V_1b_st^{2h+k}u^4 ,
\end{aligned}
\tag{4}
$$
其中 $V_0=(d^{-C_D}Q)|_C e^3$，完整 $V_1$ 按 R502 保留。
特别不能先在 raw $\bar\Gamma$ 中删除 $\zeta^3$ 或 $V_1$。

将 (3) 乘入 (4)。原第三块的起点是
$t^{k+1}=t^\ell$，所以第三块准确为零。
由 $m(t,\psi e^{\eta+a\epsilon})$ 的第一 $\epsilon$ 系数新产生的第三块，
其 $t$ 阶至少为 $h+k+1=h+r\ge\ell$，也准确为零。
第一块仍为零，第二块最初 $r$ 行亦为零。

因此这一次无需原 $L_\beta$ 的低行右逆：
乘后目标本来就在原低行的共同零空间中。
不能先将旧未乘目标减去 $L_\beta$，
然后把 $\mu L_\beta$ 当成已回到同一来源的列。

用 R552 的同一个高目标单位
$t^{-r}\mathfrak q_{\rm phys}^{-1}$ 归一，
其中 $\mathfrak q=d^{-C_D}Q$。
在
$$
\mathcal A_T=k[[t]][\epsilon]/(t^T,\epsilon^2),\qquad \eta_0=t^hu,
$$
乘前的完整第二高块为
$$
\epsilon\left[
b_se^3u^3t^{h+k-r}
+6ae^3u\xi t^h
+\frac32b_se^2f_2u^4t^{2h+k-r}
\right].
\tag{5}
$$
(5) 包括原 $V_1$ 与物理 $Q$ 单位运输的相消，不是只取 $V_0$。

现在使用 $k=r-1$ 后再乘 $t\,m(t,\psi e^{\eta_0})$。
$f_2$ 项起于 $t^{2h}$，而 $T\le2h$，因此此时才可删除。
同样，
$m(t,\psi e^{\eta_0})-m(t,\psi)\in t^h$，
其对首 carry 的新增项也从 $t^{2h}$ 起。
于是整个乘后目标恰为
$$
\boxed{
\epsilon\,m|_C\,e^3 t^hu
\{b_su^2+6at\xi\}\pmod{t^T}.}
\tag{6}
$$

以原接触尾单射
$$
\iota_\xi(x)=2ae^2\eta_0\epsilon x
$$
表示，得到实际短行
$$
\boxed{
\overline{\mu J(P^{\rm fact})/p}
\longleftrightarrow \iota_\xi(x),\qquad
x=(m|_C)e\left(\frac{b_su^2}{2a}+3t\xi\right)
\bmod t^q .
}
\tag{7}
$$
箭头仅表示上述已付原低行和高像单位规范，没有给来源加列。

如果进一步处于 R552 的几何范围 $h>\kappa$、$q>\kappa$，
其中 $\kappa=C^2$，则全部原列的准确判据为
$$
\overline{\mu J(P^{\rm fact})/p}\in\operatorname{im}\bar J
\quad\Longleftrightarrow\quad [x]=0
\text{ 于同一个 }D_\xi^{\rm actual}.
\tag{8}
$$
(8) 使用 R552 的共同核 $W^0$，包括全部 $\mathcal W_D$ 列。
$x(0)$ 为单位本身不判非零；原 $\mathcal H_1$ 有在指定点取单位的实际截面。

## 3. q 条行只需同一因子的截止内 forcing

原算子和有理项为
$$
\mathcal P=6(1-t)\delta^2-(1+2t)\delta,\qquad
\mathcal R=\frac{t(154+160t+1792t^2)}{3(1+8t)^2}.
$$
同一因子给完整有理分支 forcing
$$
\mathcal F_{\widetilde F}
=\mathcal R-\{6(1-t)\delta-(1+2t)\}
\left(-\frac{t\widetilde F_t}
{Y\widetilde F_Y}\bigg|_{\widetilde C}\right).
\tag{9}
$$
R507 的准确 Gaussian 修正从 $t^s$ 起。
因此全部 $n<s$ 的系数满足
$$
\boxed{
c_n=\frac{\mathcal F_{\widetilde F,n}
+2(n-1)(3n-2)c_{n-1}}{n(6n-1)},\qquad
c_n=[t^n]\eta .
}
\tag{10}
$$
$n(6n-1)$ 在 $1\le n<s$ 为单位，$c_0$ 不进入 (10)。

(7) 中的 $u\bmod t^q$ 只读
$c_h,\ldots,c_{h+q-1}$；其最后一行是
$h+q-1=s-r-1<s$。
$t\xi\bmod t^q$ 只读 $c_n/p$，$0\le n\le q-2<h$。
其中 $n\ge1$ 的低项由同一个 (9) 的整除 $p$ 结果读取，
$n=0$ 项由第1节保留的同一分支常数读取；
不能将它们作为可调的 $\xi$ 参数。
所以 (7) 的所有 q 行可由同一 $\widetilde F$ 的分支常数与有限真实递推求出，
而不需要额外指定共振后的 sigma 系数。

另保原参数中的固定曲线常数 $b=17$。
R507 的
$$
w=-(t/b)\mathsf h(t)^6,\qquad
\mathsf h(t)=\sum_{n\ge0}\frac{(1/2)_n}{n!(6n+1)}t^n
$$
给
$$
b_s=(-b)^s\mathsf h^{-p-1}
\equiv(-b)^s\mathsf h^{-1}\pmod{p,t^q}.
\tag{11}
$$
因为 $q<p$，$\mathsf h^p\equiv1\bmod t^q$。
这里只使用所需的整低窗，原 $t/w$ 单位没有省成一。

## 4. r=1 时可以使用的具体全来源矩阵

若 $r=\ell=1$，则 $T=2h,q=h$。
原 $t=0$ 只有 charge $0,1,2$ 有合法常数列；
更高 charge 由原 $A_n=\lfloor(n+1)/4\rfloor$ 至少含一份 $t$。
低三个行是这三 charge 的单位 Vandermonde。
所以其共同核准确是
$$
\mathcal W_D\cap t\,k[t,Y,d^{-1}].
\tag{12}
$$
对该共同核中的真实 $R$，定义
$$
H_R=d^{C_D}R/(tQ),\qquad H_i=(\mathcal E^iH_R)|_C .
$$
$Q(P)$ 为单位，故它是原目标中合法的局部单位规范，
不是把 $R/(tQ)$ 当作新增全局来源。
当 $T=2h$，其完整高像为
$$
(H_0+\eta_0H_1,\quad a(H_1+\eta_0H_2)).
\tag{13}
$$
它等于 (7) 当且仅当同一个 $R$ 满足
$$
\boxed{
H_0=0\bmod t^{2h},\qquad H_1=0\bmod t^h,\qquad
\frac{H_1+\eta_0H_2}{2e^2\eta_0}=x\bmod t^h .
}
\tag{14}
$$
证明中由第二式先知第一坐标的 $\eta_0H_1$ 消失；
反向直接代回 (13)。
(14) 给全部原列上的一个明确有限矩阵，
但未证明其指定右端在像中或不在像中。

$r\ge2$ 时 (12) 不能替换为所有来源都含 $t^r$：
在 $t^1$ 及以后已有更多合法 charge，
三个低矩不能逐个消去它们。
一般 $r$ 必须保 R552 的完整低行共同核，不作该非法除法。

## 5. 完整 M 和同 R 的边界

本 note 的 (7) 是完整相对 $J$ 的首层目标，
不替代原 $M=c_*U_0w^{13}J$。
若实际解决 (8) 或 (14)，还须恢复同一个 $R$ 的两条十三行 carry。
R697/R701 的非单位乘子成本、顶 charge 截断、
原 $P_{134}/U_0$、$U_1/p$ 和第三位同修正 $d_2$ 均保持。

这里没有证明两原完整中央零迫 (8) 失败，
也没有从首系数单位或短行数宣称整个余类非零。
当前留下的具体问题是：
(7) 给出的实际 q 行，在 (14) 或其一般 r 的全原列共同像中能否被吸收。

依赖：[R502](../results/R502-full-low-ell-bockstein-and-actual-geometric-residue.md)；
[R507](../results/R507-original-euler-resonance-and-actual-forcing-transpose.md)；
[R552](../results/R552-full-third-source-contact-tail-and-actual-affine-forcing.md)；
[R697](../results/R697-full-third-normal-top-reduction-and-same-correction-cap.md)；
[R701](../results/R701-sharp-two-charge-clearing-and-complete-same-correction-cap.md)。
