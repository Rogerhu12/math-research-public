# R703 — 原全迹的完整 Hall 相位及有限 Fourier 返回

日期：2026-11-15。**状态：以下完整相位、原迹恒等和 Fourier 返回已证明；非平凡指数和界及原迹非零仍未证明。**

本篇将 R696 的同一个全 $H$ 迹写成一条完全指定的有限和。
其 $p^2$ 提升相位由原除点式和真正 Hall 群作用决定，
不是给每个点另选一个方便的 $p$ 次根。
原固定 theta 幅度的离散 Fourier 系数具有一致的 $O(\log^2p)$
总变差，因此任何对这里实际有限和的统一幂次节省都能直接改进 R700。
本篇没有将通常模 $p$ 二次曲线的 Weil 界用于这条含原 $p^2$ 相位的和。

## 1. 原坐标、准周期及符号

保持 R694/R696/R700 的
$$
p=6s-1>101,\quad q=p^2,\quad d=p+1,\quad
E:y^2=x^3+17,\quad K_0=\mathbf Q(\omega).
$$
取原不变微分的复周期格
$$
\Lambda=\Omega(\mathbf Z+\mathbf Z\omega),\qquad
\delta=\omega-\omega^2=1+2\omega.
$$
对 $u=c+d_0\omega,\ v=a+b_0\omega$ 定义
$$
[u,v]=cb_0-d_0a
=\frac{\bar u v-\bar v u}{\delta},\qquad
\chi(v)=(-1)^{a+b_0+ab_0}.
\tag{1}
$$
这里 $b_0,d_0$ 是整数坐标，曲线参数仍为 17。

令 $z_v=\Omega v/p$，$v\bmod p\ne0$，并记
$$
k_v=\mathfrak k(z_v),\qquad
\mathfrak k(z)=e^{-\eta_z z/2}\sigma(z).
$$
R700 的 Legendre 归一给
$$
\boxed{
\mathfrak k(z_v+\Omega u)
=\chi(u)\exp\!\left(\frac{\pi i[u,v]}p\right)k_v.
}
\tag{2}
$$
这与 $\sigma\sim z$、$\sigma(2z)=-2y\sigma(z)^4$ 是同一个规范。

仍用原
$$
\alpha=\omega^2+p\omega,\quad \nu=p^2-p+1,\quad n=p+1,
\qquad
a_{T_v}=\psi_\alpha(T_v)^{2s}/\psi_n(T_v)^{2s-1}.
\tag{3}
$$
$\zeta_{p^j}$ 在本篇复嵌入中表示 $\exp(2\pi i/p^j)$；
其代数共轭由真正 Galois 作用运输。

## 2. 原绝对根的显示相位

准确有
$$
\alpha z_v=\omega^2z_v+\Omega\omega v,\qquad
nz_v=z_v+\Omega v.
$$
(1) 给 $[\omega v,\omega^2v]=N(v)$。
又 $\mathfrak k(\omega^2z)=\omega^2\mathfrak k(z)$，故
$$
\psi_\alpha(T_v)
=\omega^2\chi(\omega v)
 \exp\!\left(\frac{\pi iN(v)}p\right)k_v^{1-\nu},
\qquad
\psi_n(T_v)=\chi(v)k_v^{1-n^2}.
\tag{4}
$$
(4) 尤其保原偶 $n$ 除点式的符号。

因为 $2s$ 为偶数、$2s-1$ 为奇数，原 Bezout 指数为 $-p$，
所以 R694 的 $\xi_T$ 在这些代表下准确是
$$
\boxed{
a_{T_v}=\xi_v k_v^{-p},\qquad
\xi_v=\omega^{4s}\chi(v)\zeta_p^{sN(v)}.
}
\tag{5}
$$
由 $p\equiv-1\bmod6$，可明确取
$$
\boxed{
\rho_v=\omega^{-4s}\chi(v)\zeta_{p^2}^{sN(v)},\qquad
w_v=\rho_v/k_v,\qquad w_v^p=a_{T_v}.
}
\tag{6}
$$
R696 已保证这个根在 $F_2=K_0(E[p^2])$。
(6) 不是声称 $\rho_v$ 或 $k_v$ 分别都在 $F_2$；
它们先在 R694 的完整层域中解释，其组合按 R696 下降。

换代表 $v\mapsto v+p\ell$ 时，(2)、(6) 给
$$
\boxed{
\frac{w_{v+p\ell}}{w_v}
=\zeta_p^{\,s\operatorname{Tr}(v\bar\ell)
                  +(p-1)[\ell,v]/2}.
}
\tag{7}
$$
这个原 $p$ 次单位根一般不为 1。
因此仅由 $N(v)\bmod p$ 相同，不能删除代表选择产生的相位。

## 3. 真正 Hall 提升，不是任意范数一代表

置
$$
F=K_0(E[p]),\quad F_2=K_0(E[p^2]),\quad
A=K_0(E[12p^2]).
$$
R696 已证明 $F_2/K_0$ 在 $p$ 唯一且完全分歧，群为
$(\mathbf Z[\omega]/p^2)^\times$。
另一方面，原曲线在 $p>101$ 好约化，$12$ 在该位可逆，
所以 $K_0(E[12])/K_0$ 在 $p$ 不分歧。
任何两域的交同时在 $p$ 完全分歧和不分歧；
又交域在 $p$ 仍只有一个位，因此
$$
\boxed{F_2\cap K_0(E[12])=K_0.}
\tag{8}
$$

模 $p$ 的 $H=\ker N$ 阶为 $p+1$。
其在 $(\mathbf Z[\omega]/p^2)^\times$ 中的唯一阶 $p+1$
提升记为 $\widehat H$。
它是 Teichmüller 提升，满足
$$
\widehat h^{p+1}=1,\qquad N(\widehat h)=1\bmod p^2.
\tag{9}
$$
由 (8) 将其在 $A$ 中延拓为对 $E[12]$ 恒等的群。
对应完整层作用 $h_N\in(\mathbf Z[\omega]/12p^2)^\times$ 为
$$
h_N\equiv1\bmod12,\qquad h_N\equiv\widehat h\bmod p^2.
\tag{10}
$$
它的行列式准确为 1 模 $12p^2$，因而固定整个
$\mu_{12p^2}$。

注意 (9) 强于任取 $N(h)\equiv1\bmod p$ 的整数提升。
即便只补 $N(h)\equiv1\bmod p^2$，仍有 $p$ 个提升；
本篇使用其中真正阶 $p+1$ 的群提升。

## 4. 完整 Klein 比的 Galois 作用及绝对公共因子

原 Klein 比是完整层 $12p^2$ 的模函数，见 R694§3。
对行列式一的层变换，Klein/Siegel 的共同乘子在比中准确消去。
具体地，Streng 的 Lemma 2.13(6) 给
$h_{\mathbf a}(M\tau)=\epsilon(M)h_{\mathbf aM}(\tau)$，
其中 $\epsilon(M)$ 与 $\mathbf a$ 无关。
在原完整层点上评价，得到
$$
\boxed{
\widehat h(k_v/k_u)=k_{h_Nv}/k_{h_Nu}
\quad(u,v\bmod p\ne0).
}
\tag{11}
$$
这使用真正层点的 Galois 作用和 (10) 的行列式一条件；
未在 $j=0$ 曲线上忽略额外自同构，也未只取某个幂后再随意开根。

因此对固定 $\widehat h$ 存在与 $v$ 无关的公共因子 $c_h$，使
$$
\widehat h(k_v)=c_h k_{h_Nv}.
\tag{12}
$$
其绝对值和相位都能直接确定。
由原倍点
$$
k_{2v}/k_v=\Psi_2(T_v)k_v^3
$$
及 (11)，并用 $\widehat h(\Psi_2(T_v))=\Psi_2(T_{h_Nv})$，
得 $c_h^3=1$。
另一方面，(10) 保 $\chi(v)$，
(9) 保 $N(v)\bmod p$，且 $\widehat h$ 固定 $\mu_{6p}$，
所以 (5) 给 $c_h^p=1$。
因 $(3,p)=1$，
$$
\boxed{
c_h=1,\qquad \widehat h(k_v)=k_{h_Nv}.
}
\tag{13}
$$
同时 (9)–(10) 保 (6) 的整个 $\rho_v$，包括 $p^2$ 部分。
故
$$
\boxed{
\widehat h(w_v)=w_{h_Nv}.
}
\tag{14}
$$

(10) 的群限制到共同 $W=F(w_v)$ 后，正是 R696 的唯一
阶 $d$ Hall 子群 $\widetilde H$：
其在 $F$ 上仍为 $H$，且阶不减少。
于是 (14) 的原相对根与 R696(15) 完全相同，
没有残留可自由选择的 $H\to\mu_p$ 相位。

## 5. 全迹成为同一 theta 函数的规范采样和

对原 $m=34,72$ 定义固定光滑 theta 幅度
$$
\mathcal A_m(v/p)
=\mathfrak k(\Omega v/p)^m\phi_m(T_v).
\tag{15}
$$
它在格点处按零阶 6 延拓，故在整个复平面光滑；
其模的固定界已在 R700 支付。

由 (14)，原完整迹准确为
$$
\boxed{
\mathcal T_{m,T_v}
=\rho_v^{-m}\sum_{\widehat h\in\widehat H}
       \mathcal A_m(\widehat h v/p).
}
\tag{16}
$$
右端仍有全部 $p+1$ 项。
由于 $m$ 为偶数，$\mathcal A_m((v+p^2\ell)/p)
=\mathcal A_m(v/p)$，所以求和只需模 $p^2$ 的提升；
这不撤销第4节为确定 Galois 相位而使用的完整 $12p^2$ 层。

## 6. 把 p² 提升化为一个显示的模 p 相位

对 $v\in\mathbf Z[\omega]$ 定义
$$
t_p(v)=\frac{v^{p^2}-v}{p}\bmod p,\qquad
\tau_m(v)=\frac m2[t_p(v),v]\in\mathbf F_p.
\tag{17}
$$
系数除 $p$ 合法，因为剩余域为 $\mathbf F_{p^2}$。
这里计算的是原整数代表的 $p^2$ 精度，并未只保其模 $p$ 值。

还有较短的等式
$$
\boxed{
\tau_m(v)=\frac{m}{2\delta}
            \frac{v^{p+1}-\bar v^{\,p+1}}p\bmod p.
}
\tag{18}
$$
确实 $v^p\equiv\bar v\bmod p$，且
$v^{p^2}\equiv\bar v^{\,p}\bmod p^2$。
将此代入 (17) 的交错积即得 (18)。
(18) 是对整数代表先作整除再约化；
不能把它误读成固定低次数的 $\mathbf F_p$ 多项式。

令 $u$ 为 $\widehat h v\bmod p$ 的选定整数代表。
Teichmüller 乘法性给
$$
\widehat h v
\equiv u+p\left(t_p(u)-\frac{t_p(v)}v\,u\right)\pmod{p^2}.
$$
又 $N(u)=N(v)\bmod p$。
利用交错积在乘法下按范数缩放，(2) 遂给
$$
\boxed{
\mathcal A_m(\widehat h v/p)
=\zeta_p^{\tau_m(u)-\tau_m(v)}\mathcal A_m(u/p).
}
\tag{19}
$$
这一步使用的是整个 Teichmüller 提升，而非另选范数一坐标。

对每个 $u=a+b_0\omega\bmod p$ 固定代表
$0\le a,b_0<p$，记 $r=N(v)\bmod p\in\mathbf F_p^\times$。
原全迹最终成为
$$
\boxed{
\mathcal T_{m,T_v}
=\rho_v^{-m}\zeta_p^{-\tau_m(v)}
   \mathscr S_{p,m}(r),
\quad
\mathscr S_{p,m}(r)=
\sum_{\substack{u\in\mathbf F_{p^2}\\N(u)=r}}
  \zeta_p^{\tau_m(u)}\,\mathcal A_m(u/p).
}
\tag{20}
$$
这是无未知相位的精确恒等。
所有 $p^2$ 信息都在显示的 $\tau_m$ 和前面的根单位中。

### 换代表的完整抵消

若 $u\mapsto u+p\ell$，则
$$
t_p(u+p\ell)\equiv t_p(u)-\ell\pmod p,\qquad
\tau_m(u+p\ell)-\tau_m(u)=-\frac m2[\ell,u].
$$
而 (2) 给
$$
\mathcal A_m((u+p\ell)/p)
=\zeta_p^{(m/2)[\ell,u]}\mathcal A_m(u/p).
$$
所以 (20) 每个乘积项严格不变。
不能单独更换 $\tau_m$ 的代表而保持幅度不动。

原 $\mu_6$ 对称使六个点的完整项相同；
复共轭使 $\tau_m$ 变号、幅度取共轭。
因此 $\mathscr S_{p,m}(r)$ 是实数，并可准确按六点轨道合并。
这仍不保证它正或非零。

## 7. 固定幅度的完整有限 Fourier 公式

在单位方形上写
$$
A_m(x,y)=\mathfrak k(\Omega(x+y\omega))^m
          \phi_m(P(\Omega(x+y\omega))).
$$
这是一个固定的光滑函数，包括四个格点角的零阶 6 延拓。
它一般有非平凡边界相位，不能假定是一个普通周期函数。

对其实际 $p\times p$ 样本作离散 Fourier 变换：
$$
\widehat A_{m,p}(k,l)
=\frac1{p^2}\sum_{a,b_0=0}^{p-1}
 A_m(a/p,b_0/p)e_p(-ka-lb_0).
\tag{21}
$$
定义完全指定的有限和
$$
K_{p,m}(r;k,l)=
\sum_{\substack{0\le a,b_0<p\\a^2-ab_0+b_0^2=r\ (p)}}
 e_p\bigl(\tau_m(a+b_0\omega)+ka+lb_0\bigr).
\tag{22}
$$
有限 Fourier 反演给
$$
\boxed{
\mathscr S_{p,m}(r)
=\sum_{k,l\bmod p}\widehat A_{m,p}(k,l)
                     K_{p,m}(r;k,l).
}
\tag{23}
$$
没有截断 theta 展开，也没有删去高 Fourier 模式。

### 全部 Fourier 系数的一致总变差

令 $k_*=\min(k,p-k)$、$l_*=\min(l,p-l)$，
其中 $0\le k,l<p$。
存在只依固定 $A_m$ 的常数 $C'_m$，使
$$
\boxed{
|\widehat A_{m,p}(k,l)|
\le\frac{C'_m}{(1+k_*)(1+l_*)}.
}
\tag{24}
$$
证明用两次有限循环差分。
内点的差分由一阶、混合二阶导数控制；
跨过方形边界的跳跃保留为边界值差。
一次循环差分在一条长度 $p$ 的线上绝对值总和为 $O_m(1)$，
混合循环差分在全 $p^2$ 点上的绝对值总和也为 $O_m(1)$：
内点给 $p^2O_m(p^{-2})$，两条边各给
$pO_m(p^{-1})$，四角给 $O_m(1)$。
故非零 $k,l$ 时
$$
|\widehat A(k,l)|
\le \frac{O_m(1)}
 {p^2|1-e_p(k)||1-e_p(l)|},
$$
由 $|1-e_p(k)|\ge4k_*/p$ 得 (24)；
只有一个或没有非零频率时用一次或零次差分。
此证明明确保边界跳跃，未使用错误的周期性。

于是
$$
\boxed{
\sum_{k,l\bmod p}|\widehat A_{m,p}(k,l)|
 \le C''_m(1+\log p)^2,
\qquad
|\mathcal T_{m,T_v}|
\le C''_m(1+\log p)^2
      \max_{k,l}|K_{p,m}(r;k,l)|.
}
\tag{25}
$$
全部绝对嵌入也满足对所有 $r\ne0$ 取最大值的同一界；
R700 已支付共轭原曲线和根单位的模。

## 8. 已付的平方平均与尚未付的最大值

(22) 中相位均有模一，范数二次曲线有 $p+1$ 个点。
只用加法字符正交性就得
$$
\boxed{
\sum_{k,l\bmod p}|K_{p,m}(r;k,l)|^2=p^2(p+1).
}
\tag{26}
$$
因此其均方根准确是 $\sqrt{p+1}$。
(26) 不是对最大值的平方根界，不能从这里推出 (25) 的幂次节省。

若未来对这批**指定**和证明某个固定 $\epsilon>0$ 的
$$
\max_{\substack{r\ne0\\k,l}}|K_{p,m}(r;k,l)|
\ll_m p^{1-\epsilon},
\tag{27}
$$
则 (25)、R700 的固定分母及唯一 $p$ 位给非零原边界
$$
v_p(\mathcal B_m(v_T^d))
\le1-\epsilon+
 \frac{2\log(1+\log p)+O_m(1)}{\log p}
 -\frac1{p-1}.
\tag{28}
$$
这是对原同一个边界的合法接口，不增加新的中央零。

本篇没有证明 (27)。
$\tau_m$ 保留原 Teichmüller $p^2$ 提升，
在 (18) 中先整除 $p$ 再约化；
它不是可以直接用通常固定次数 conic Weil 界处理的裸线性或二次相位。
同样不能把任意模 $p^2$ 范数一提升代入 (22)。
可继续检验 Heilbronn/Witt 和或完整有限 Weil 表示，但须匹配 (17)–(22)。

## 依赖与原始来源

- [R694](R694-original-cm-kummer-descent-and-full-norm-one-trace.md)：
  原 Klein/Siegel 规范、完整层模函数及原相位。
- [R696](R696-original-absolute-roots-p2-field-and-linear-height-trace.md)：
  $F_2$ 全局次数与唯一 $p$ 位、共同 $W$、Hall 子群、同一个原迹。
- [R700](R700-original-fixed-denominator-and-logarithmic-trace-height.md)：
  固定分母、全部复共轭、原边界高度接口。
- Marco Streng, *Generators of the group of modular units for
  $\Gamma^1(N)$ over the rationals*, Annales Henri Lebesgue 6 (2023),
  95–116，§2.2.2、Lemma 2.13(3),(6)：
  [期刊原文](https://numdam.org/item/10.5802/ahl.160.pdf)。
  本篇仅用其完整 Klein/Siegel 变换式；
  第4节另外支付实际 Hall 行列式、公共因子和绝对根相位。

本篇没有数值扫描或新增可重算数据文件。
