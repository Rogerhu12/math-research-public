# R119 续篇：非解背景的准确散度 Jacobi 差与窄径向残差乘积

2026-11-15，visible-exact / tail_connector。

**状态：已证明。** 在原 fixed-stop 度量及原
$\mu_j,\zeta_j,C_j$ 上，本文明确区分任意有限角近邻场的真实
Darboux 线性化与几何对称散度算子。二者的差不是零；
它准确是一阶、含当前完整 residual 的算子。
转到原普通源单位后，该差不增加任何 $\delta_j$ 的逆幂。
这给采用几何近似 Newton 算子时必须支付的真实缺陷，
并完整保留 nonlinear mean、metric 参考高度和 $+\psi N$。

此处不把已有已知解背景上的全网络 inverse 转授给任意近邻背景。
本文给的是准确算子身份、普通窄源的 tame 费用及真正二次误差；
后继仍须构造相应变化背景的 inverse 和完整迭代。

## 1. 原变量与非零 residual

采用 [有限角 mean/height 图](R119-supplement-finite-Sobolev-nonlinear-holonomy-charge-and-height-chart.md)
M.7--M.18 和 M.32--M.37 的真实物理变量。
$t=\log a_{\rm ph}$，尾上 $a_{\rm ph}=\rho r$，$w>0$，
$A=(\log w)_t$、$Q=-A$。令
$$
 U=P_\theta,\quad V=K_\theta,\quad q=w^2,\quad E=1+q,\quad
 L=1+K,\quad J=L+EU,
$$
$$
 D=1-q(2K+K^2+EP^2),\qquad
 A_0=JD^{-3/2},\qquad
 d=\frac{E(V-P)}J,\qquad v^2=\frac D{J^2}.
 \tag{O.1}
$$
这里 $A_0$ 是密度因子，不能与 metric 的 $A$ 混用。
实小球给 $D,J>1/2$。背景来自一个真实高度，因而准确满足
$$
 P_t=V-(A+1)P,\qquad
 K_t={\cal F}(P,K,U,V)+\mathfrak r ,
$$
$$
 {\cal F}=\frac{-A(2K+U+K^2+KU+qP^2)+E(V-P)^2}{J}.
 \tag{O.2}
$$
$\mathfrak r$ 不要求为0；它可为实际 nonlinear residual，
或给定的 ordinary 体源。允许真实径向分片，所有高度和一阶迹按
同一原图匹配。假定所用 $K_t,\mathfrak r_\theta$ 是局部可积的
普通函数。以下恒等式由光滑逼近也在这个分布范围成立。
未将径向原子背景或不明 bare weak 端迹收入这个普通源 norm。

对于固定 metric 的真实高度方向 $h$，写
$$
 p=\frac{h_\theta}{a_{\rm ph}w},\qquad
 k=\frac{h_t}{a_{\rm ph}w},\qquad
 {\cal L}_Wh=k_t-{\cal F}_Pp-{\cal F}_Kk
                    -{\cal F}_Up_\theta-{\cal F}_Vk_\theta .
 \tag{O.3}
$$
这是完整原方程的 Fréchet 线性化。它保所有 Fourier 模及 mean。

## 2. 两个准确传输恒等式

置 $T=2K+U+K^2+KU+qP^2$、$H=V-P$。
直接求导给
$$
 {\cal F}_P=-\frac{2AqP+2EH}{J},\qquad
 {\cal F}_K=-\frac{A(2L+U)+{\cal F}}J,
$$
$$
 {\cal F}_U=-\frac{AL+E{\cal F}}J,\qquad
 {\cal F}_V=2d,\qquad
 {\cal F}_U+d^2=Qv^2 .
 \tag{O.4}
$$
最后一式只用 $LJ-ET=D$，完全不依赖 $\mathfrak r=0$。

$E_t=2Aq$、(O.2) 给
$$
 J_t={\cal F}+\mathfrak r+EV_\theta+
                         \{A(q-1)-E\}U,\qquad
 D_\theta=-2q(LV+EPU).
$$
将 $D_t$ 中的 $K_t$ 写成 $\mathcal F+\mathfrak r$，准确得到
$$
 \boxed{\quad
 D_t-dD_\theta=\frac{2AqUD}{J}-2qL\mathfrak r .
 \quad}                                                   \tag{O.5}
$$
一项可直接核的化简如下：$- (D_t-dD_\theta)/(2q)$ 等于
$$
 A(L^2-1+qP^2)+L{\cal F}+L\mathfrak r+EPH
                    -\frac{EH}{J}(LV+EPU).
$$
其中 $PJ-LV-EPU=-LH$，所以 $EH^2$ 两项消去；
其余是 $AU(ET/J-L)+L\mathfrak r=-AUD/J+L\mathfrak r$。
证明没有除以 $Q$，在转向根 $Q=0$ 也成立。

令真实密度
$$
 \mu=\frac w{a_{\rm ph}}A_0 .
$$
记
$\alpha=J^{-1}+3qL/D$、$\beta=E/J$、$\gamma=3qLd/D$。
由 (O.5) 及 $d_\theta$ 的准确导数，
$$
 (\log\mu)_t-d_\theta-d(\log\mu)_\theta
                 =-(A+1+{\cal F}_K)+\alpha\mathfrak r .
 \tag{O.6}
$$
例如左侧先化成
$A-1+(\mathcal F+\mathfrak r+A(q-1)U)/J
 -\tfrac32(D_t-dD_\theta)/D$，再用 (O.4) 即得。

若将所有 $K_t,V_t$ 暂分别代为 $\mathcal F,\mathcal F_\theta$，
同一 (O.4) 直接给第二个一阶系数 $-\mathcal F_P$。
恢复真实 residual 时
$$
 \Delta d_t=\beta\,\mathfrak r_\theta-\frac dJ\mathfrak r,
 \qquad \Delta(\log\mu)_t=\alpha\mathfrak r.
$$
因此第二个完整系数恰为
$$
 -d_t-d(\log\mu)_t-(Qv^2-d^2)_\theta
               -(Qv^2-d^2)(\log\mu)_\theta
   =-{\cal F}_P-\beta\mathfrak r_\theta-\gamma\mathfrak r .
 \tag{O.7}
$$
为核清暂代部分，利用 $\mathcal F_U=- (AL+E\mathcal F)/J$，
$\mathcal F_\theta$ 与 $J_\theta$ 的项先准确消去。
再用 $\mathcal F_U+d^2=-AD/J^2$ 和 (O.5) 的零 residual 部分，
剩下
$$
 d_t+d(\log\mu)_t+(\mathcal F_U)_\theta
                  +\mathcal F_U(\log\mu)_\theta
 =\frac{-2EV+(2E-2Aq)P}{J}=\mathcal F_P .
$$
具体地，涉及 $D$ 的两项合成 $-3AqV/J$；
其余项中 $V$ 的 $+3AqV/J$ 正好抵消。
这给 (O.7) 的完整核对，而不是引用已知解上的形式自伴性。
其中 $\gamma$ 的正定义与右侧的负号必须同时保持。

## 3. 真线性化与几何散度算子的完整差

在当前同一个真实背景定义
$$
 G=\mu
 \begin{pmatrix}
 1&-d\\-d&d^2-Qv^2
 \end{pmatrix},\qquad
 {\cal J}_Wh=\frac1{w^2A_0}\operatorname{div}_{t,\theta}(G\nabla h).
 \tag{O.8}
$$
这是对称散度型的几何算子；$\mu a_{\rm ph}w=w^2A_0$。
由 (O.3)--(O.7)，准确有
$$
 \boxed{\quad
 {\cal J}_Wh={\cal L}_Wh+
     \alpha\mathfrak r\,k-\beta\mathfrak r_\theta\,p
                                      -\gamma\mathfrak r\,p .
 \quad}                                                   \tag{O.9}
$$
完整差只含高度的一阶 $p,k$，但不能因为当前 $\mathfrak r$ 小
便把它删除。特别任意近邻背景的 $\mathcal L_W$ 不在本文中被称为
原来的自伴散度算子。其 principal 两支仍由 (O.4) 给出，
这和两算子有相同主部并不矛盾。

实背景的 $G$ 给真正 Green 配对，bare conormal 是
$\mu(h_t-dh_\theta)$。若线性方程另带 weak 径向势 $F^t$，
total conormal 仍是 $\mu(h_t-dh_\theta)+F^t$。
(O.9) 把显示的差作为额外 ordinary 源时，不改变这个真实配对，
也不允许由体源 norm 推断 $F^t$ 的 bare 端迹。
源的相邻胞单位变换、两个独立物理 mean 及外 $C_R/B_0$ 都保持原定义。

## 4. 原窄源单位中没有新的径向逆幂

写
$$
 c_{\rm phys}=\frac{\mu_jp_*^2}{12r^{10}},\qquad
 N=c_{\rm phys}\mathfrak r,\qquad
 {\cal E}_N[h]=c_{\rm phys}({\cal J}_W-{\cal L}_W)h .
$$
$c_{\rm phys}$ 是原径向标量，不依赖角。
因此 (O.9) 等价于
$$
 \boxed{\quad
 {\cal E}_N[h]=\alpha Nk-\beta N_\theta p-\gamma Np .
 \quad}                                                   \tag{O.10}
$$
不存在 $N_t$，不存在除以 $w^2$ 后新出现的 $\delta_j$ 费用，
也不存在不说明的 Fourier cutoff。

使用原新径向 norm
$$
 {\mathfrak Y}_s(h)=\sup_j C_j^{-1}\sup_{I_j}
               \|(p,k,p_\theta,k_\theta)\|_{H^s},\qquad
 {\mathfrak N}_s(N)=\sup_j(\zeta_j\delta_j^{16})^{-1}
                                  \sup_{I_j}\|N_j\|_{H^s}.
 \tag{O.11}
$$
取一个有限角近邻背景，满足
$\sup_jC_j^{-1}\sup_{I_j}\|(P,K_\perp,U,V)\|_{H^{66}}\le2^{-24}$，
并由 M 的真小根补全 $K$，$|c|\le2^{32}\sigma_j$；
本篇主相位的 $c=0$ 子域当然包含在内。
M.4 及 tame 小根给完整 $K$ 同样很小。
于是 $\alpha,\beta,\gamma$ 的 $H^s$ 及乘法 tame 常数，
$0\le s\le64$，可统一取 $2^{4096}$。
证明是原可去商与
$\|z^n\|_{H^s}\le n^s(2\|z\|_{H^1})^{n-1}\|z\|_{H^s}$
的完整级数；只用 $q<1/4,D,J>1/2$，不需要背景角解析。

令 $s^\flat=\max(s,2)$，$s^\sharp=\max(s+1,2)$。
完整 Sobolev 乘积和 (O.10) 给
$$
 \mathfrak N_s({\cal E}_N[h])
 \le2^{8192}\left(\sup_jC_j\right)
 \left\{
  \mathfrak Y_{s^\flat}(h)\mathfrak N_2(N)
    +\mathfrak Y_2(h)\mathfrak N_{s^\sharp}(N)
 \right\},\qquad0\le s\le64 .
 \tag{O.12}
$$
右边的 $s^\sharp=s+1$ 只来自真实 $N_\theta$，没有混入径向
缩域或未付 mean 费。可由
$\|fg\|_{H^s}\le2^{s+1}
(\|f\|_{H^s}\|g\|_{H^1}+\|f\|_{H^1}\|g\|_{H^s})$
逐项得到。各胞的 $\zeta\delta^{16}$ 准确消去，保留方向态的
$C_j$；用 $\sup C_j<2^{-12}$ 也合法，但不是新增几何小参数。

(O.12) 是普通强方向的门。若 $h$ 是仅有 BV/测度端口的解，
须对其真实一侧迹与测度项另行收费；本文不把 (O.12) 扩大成
对任意 weak 原子的免费普通源估计。

## 5. 真 mean 方程中的缺陷也准确配对

在固定 metric 上，对同一完整 $A_0$ 取方向导数：
$$
 DA_0[p,k]
 =A_0\left\{\alpha k+\frac{3qEP}{D}p+\beta p_\theta\right\}.
 \tag{O.13}
$$
(O.1) 直接给
$$
 (A_0\beta)_\theta-A_0\gamma
                      =A_0\frac{3qEP}{D}.
$$
事实上 $A_0\beta=ED^{-3/2}$，用 (O.5) 前的 $D_\theta$
即可验证右侧，完全没有用 $K_t=\mathcal F$。
对完整圆周作一次分部积分，于是
$$
 \boxed{\quad
 \left\langle A_0{\cal E}_N[h]\right\rangle
                    =\left\langle N\,DA_0[p,k]\right\rangle .
 \quad}                                                   \tag{O.14}
$$
右侧含 $N$ 的全部 mean 及所有非mean配对；没有把 $N$
预先投影成均值零。

令 M 文中的真实 holonomy charge 为 $\chi=\mathcal M-1$。
M.18 的准确变分是
$D\chi[h]=\langle\mu(h_t-dh_\theta)\rangle$。
由 M.16，固定 metric 而任意 residual 下，
$$
 \begin{aligned}
 (D\chi[h])_t
 &=12\mu_jr^{-4}\left\langle
       A_0c_{\rm phys}{\cal L}_Wh+N\,DA_0[p,k]\right\rangle\\
 &=12\mu_jr^{-4}
             \left\langle A_0c_{\rm phys}{\cal J}_Wh\right\rangle .
 \end{aligned}                                             \tag{O.15}
$$
其中 $q/c_{\rm phys}=12\mu_jr^{-4}$ 是原单位转换；
这里的 $\mu_j$ 不是 (O.6) 的密度 $\mu$。
(O.15) 是真实 mean 的变分恒等式，
并不把任何给定外端 charge 设为0。
有 total-conormal 源时，相应 $F^t$ 端负荷仍按原 Green 公式
一并加入；(O.15) 只说明本文显示的 ordinary 缺陷如何配对。

纯常数高度方向 $h=\lambda$ 满足 $p=k=0$，
因此 $\mathcal L_Wh=\mathcal J_Wh=\mathcal E_N[h]=0$。
这个高度规范核与 $\chi$ 的真通量方程是两个不同对象；
本文没有将其中一个代替另一个。

## 6. metric 方向与参考高度：没有漏掉 $+\psi N$

沿原两 metric bump 取 $\psi=\dot{\log w}=\dot{\log p_*}$，
并让 $h$ 表示同一固定物理坐标下的完整高度变分。
M.34--M.37 已准确给
$$
 \dot{\mathfrak r}={\cal L}_Wh-e_\psi-\psi\mathfrak r,
 \qquad
 \dot c_{\rm phys}=2\psi c_{\rm phys},
 \qquad
 \dot N=c_{\rm phys}({\cal L}_Wh-e_\psi)+\psi N .
 \tag{O.16}
$$
$e_\psi$ 包括原 $\psi_t$ 主项及完整背景系数；
不以“改变参考面”的名称将其删去。

用同一固定平端定义真实参考高度
$$
 (h_\psi)_t=a_{\rm ph}w\psi,\qquad h_\psi(t_f)=0,\qquad
 \widetilde h=h-h_\psi,\qquad
 e_{\psi,\mathrm{rem}}=e_\psi-{\cal L}_Wh_\psi .
$$
把 (O.9) 代入 (O.16)，准确得到
$$
 \boxed{\quad
 \dot N=c_{\rm phys}
       ({\cal J}_W\widetilde h-e_{\psi,\mathrm{rem}})
                    +\psi N-{\cal E}_N[\widetilde h].
 \quad}                                                   \tag{O.17}
$$
可以先对 $h$ 使用 (O.9)，再对 $h_\psi$ 使用一次；
两项 $\mathcal E_N[h_\psi]$ 正好抵消。
因此 (O.17) 既没有漏收参考高度，也没有将同一残差重复收费。
所有跨胞高度常数及原 $D\Gamma$ lift 的外端两列仍按
$h_\psi$ 的这个固定定义取值。

$\psi$ 是径向函数，故
$$
 \mathfrak N_s(\psi N)
       \le\|\psi\|_{L^\infty_t}\mathfrak N_s(N).
 \tag{O.18}
$$
另一项由 (O.12) 支付。这里没有 $N_t$，
也不必让未知普通源经过径向变化的角坐标。
metric 方向最终来自哪个参数图，是独立的选择问题：
新的 finite-Sobolev 第一相位图可以给其第一列；
第二标量相位、完整 $\Gamma$ 联立与原 $\nu$ 行
仍须各自真实付清。本式不将它们统称为一个已知小量。

## 7. 同一近邻球的真正二次余项

这里只扩展原 R.31--R.33 的**代数余项**，
不扩展 R 的变化背景 inverse。
取完整兼容高度增量 $h$，令 $Y=(p,k,p_\theta,k_\theta)$，
$j_Y=k+Ep_\theta$。在固定 metric 的同一个点，
$$
 \begin{aligned}
 e_2&={\cal F}(W+Y)-{\cal F}(W)-D{\cal F}(W)Y\\
    &=\frac{N_2-j_YD{\cal F}(W)Y}{J+j_Y},\\
 N_2&=-A(k^2+kp_\theta+qp^2)
                         +E(k_\theta-p)^2 .
 \end{aligned}                                             \tag{O.19}
$$
这里 $W$ 的 $K_t-\mathcal F$ 可以不为零；
(O.19) 只是在原准确二次分子除以原一次分母中作一次展开。
若当前背景满足第4节的球，且
$\mathfrak Y_{64}(h)\le2^{-24}$，则 $J+j_Y>1/2$。
用第4节同一完整 Sobolev 乘法级数，
$$
 \|e_2\|_{H^s(I_j)}
 \le2^{8192}(1+|Q|)\,C_j^2\,
           \mathfrak Y_{64}(h)\mathfrak Y_s(h),
                  \qquad0\le s\le64 .
 \tag{O.20}
$$
$H^s(I_j)$ 在这里表示该胞内逐真实 $t$ 的角范数上确界，
不是对径向函数另外作 $s$ 次微分。
每项至少含两个完整方向态；$Q$ 是径向原系数。
背景系数的费用已含在 $2^{8192}$，没有沿用已知解的
特殊消去来缩小这个常数。

转到原单位时，只需原径向表 R.33：
$$
 \frac{\mu_jp_*^2(1+|Q|)\,C_j^2}{\zeta_j\delta_j^{16}}
 \le2^{700}J_jh_j^{-10}\frac{\zeta_j}{\mu_j}
                                      \delta_j^{-47/2},
 \qquad J_j=j+5 .
$$
有限前缀的原两段指数和最深段的
$103-10/256>102$ 均未改变。
原表中整个有限前缀及固定全局比例的费用小于 $200000$ bits；
再单独加入本篇的 $8192$ bits 和上式 $700$ bits，
仍严格小于 $524288$ bits。因此
$$
 \boxed{\quad
 \mathfrak N_s(c_{\rm phys}e_2)
 \le2^{524288}\mathfrak Y_{64}(h)\mathfrak Y_s(h),
                         \qquad0\le s\le64 .
 \quad}                                                   \tag{O.21}
$$
$1/12$ 只改善界，未用来抵消其他未列费用。
此处没有改变原 $\zeta_j$ 的深层指数131，
也没有把有限角范数称为原 analytic224 标签。

例如，如果后继已经为当前背景构造了满足全部真实端条件的
几何校正 $h$，使
$c_{\rm phys}\mathcal J_Wh=-N$，
那么在固定 metric 上作准确的高度直线增量，真实残差满足
$$
 N(W+Y)=-{\cal E}_N[h]-c_{\rm phys}e_2 .
 \tag{O.22}
$$
这是由原方程直接相减得到的缺陷身份，
不是对这个 $h$ 的存在声明。
右侧第一项由 (O.12)、第二项由 (O.21) 付费。
如果实际更新还要经过 M 的非线性 mean 图、
第一相位图或第二 $\Gamma$ 图，
必须另加这些真实图的二阶链式余项和端点变化；
不能把上述高度直线无条件称为保持 holonomy 的完整迭代。

## 8. 已完成与后继准确接口

本文完成任意声明有限角近邻背景上的三件事：
真实线性化与几何散度算子的准确 residual 差；
该差在原窄径向普通源单位中的 tame 费用；
以及它同完整 mean 方程、metric 参考高度和真正二次余项的兼容。

后继变化背景的全网络逆仍须独立构造。
R 的已证固定背景 inverse 仍有2050导损失、
输入源最高2114阶、输出最高64阶的原范围；
本篇没有消去这些限制。
新的第一相位图也没有给出第二 scalar normal-form 系数的
非解析有限角背景定义及定量导数。
外帽、$C_R/B_0$、$\nu$、两 $\Gamma$ 与原物理端点条件
须继续在同一真实表示中联立，才能宣称完整存在性闭合。
