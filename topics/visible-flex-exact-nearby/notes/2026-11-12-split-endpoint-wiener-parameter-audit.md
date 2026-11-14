# 固定标签下的端点误差拆分、参考角图与参数接合独立核查

2026-11-12，independent-audit。供 R101 使用的完整接合证明。

本篇只证明同一实际返回、同一已保存有限端点和同一预 Newton 校正之间的误差转换。不重新生成任何 550 段数据，不宣布 R31 算术门或完整 PDE 逆已通过。R101 的新局部二阶积分界仍须引用其实际完整覆盖报告。

## 1. 来源、准确对象与有限多项式

以下文件在提交 93bbc1b548afd86ace4f397b545476172d370eb1 读取：

- scripts/fourfold_parameter_endpoint_spatial_v2.py，SHA256
  0f652c9d397ea3e91f1c293bec09e4006e71bbef3c29bbff5fb06234ba5b32fe；
- scripts/fourfold_half_return_prenewton_v2.py，SHA256
  1fcedfceaed51d955e88e035018b81137c6cfe036f1a6f701105f5a57b35b724；
- notes/2026-11-12-complete-flow-43301401638-arithmetic-summary.json，逐字节 SHA256
  f25a3692b36390b3ae8dd7699d4e0ec0c2e74561ac238b11352f1d532a8bfc52；
- data/phase_ring_continuation/step5_half_prenewton_43308150283/report.json，SHA256
  030cf8444f5a0cc5058e7ce056b2b310328e7d78a842582273ffb70d2f6f720a。

原始完整 actual_endpoint.json.gz 的 SHA256 为
f8d958ce1af4cac5d4053d8c7569d33c049a917d84094e55944842fad4228328。
这里不从摘要重新构造这份二进制报告。

全部角变量是归一化的 $2\pi$ 周期标签 $x$。令实际 half return 为
$\mathscr P_p$，冻结原共轭 $H=x+h$ 和整个时间参考。参考初端为
$H(x)/4$，末端为 $x/4+U(x)$，所以定义
$
 L(x)=x+4U(x),\quad
 \Gamma_p=\mathscr P_p\circ H,\quad
 G_p=H^{-1}\circ\Gamma_p .
$
参考对真实参数 $p$ 不变。参考坐标中的实际流 $X_p$ 因而满足准确恒等式
$
 \Gamma_p=L\circ X_p.                                      \tag{A1}
$
这已包含物理角到标签角的因子 $4$。

endpoint_three_orders_spatial 对三份保存的 $C_i+D_i$ 逐系数选准确 dyadic
中心，记为 $a_i$。这三个有限多项式不必是一个有限参数族的导数。直接核源码：
$
\begin{split}
 Q_0:=x+P_0&=L+L'a_0+\tfrac12L''a_0^2,\\
 P_1&=(L'+L''a_0)a_1,\\
 P_2&=(L'+L''a_0)a_2+L''a_1^2.                 \tag{A2}
\end{split}
$
每个有限乘积的全部频率均保留。特别地，$P_0$ 是物理端点的周期部分，
不是 $G_{p_0}$ 的周期部分；不能把 $1+P_0'$ 与 $P_0'$ 混淆。

令
$
 Z=\operatorname{id}+a_0,\quad e=X_{p_0}-Z,\quad
 \ell=L\circ Z-Q_0.                                        \tag{A3}
$
若 $\|L'''\|_{r+\|a_0\|_r}\le M_3$，则完整 Taylor 积分式给
$
 \|\ell\|_r\le M_3\|a_0\|_r^3/6.                           \tag{A4}
$
原报告中的 complete_Taylor_fees[0] 也可直接使用；它与 (A4) 是同一剩余。
较粗的 $M_3<10^{10}$、$\|a_0\|<3.017\,10^{-11}$ 已给
$\|\ell\|<5\,10^{-23}$，无需删掉此项。

## 2. 在 Wiener 代数构造真实参考图

记 $\mathcal A_s$ 为加权 Fourier $\ell^1$ 代数。对解析于闭 $\sigma$
带且 sup 不超过 $A$ 的周期函数 $u$，R63 的边界 Parseval 给
$
 \|u\|_s\le A\sqrt{1+\frac4{e^{2d}-1}}
 \le A\sqrt{1+\frac2d},\qquad d=\sigma-s.                   \tag{A5}
$
同一 Cauchy--Schwarz 直接用于导数得到
$
 \|u'\|_s\le
 2A\left(\sum_{k\ge1}k^2e^{-2dk}\right)^{1/2}
 \le \frac A d\sqrt{1+\frac1d}.                            \tag{A6}
$
最后一步使用
$\sum k^2r^k=r(1+r)/(1-r)^3$、
$r/(1-r)^2=1/(4\sinh^2d)\le1/(4d^2)$ 和
$(1+r)/(1-r)=\coth d\le1+1/d$。常数、正负模均保留。

完整实际源给
$
 \sigma=3/1024,\quad
 \|X_{p_0}-\operatorname{id}\|_{\sup,\sigma}
 <A=4.092564\,10^{-8}.
$
取
$
 t=17/8192,\quad V=1/400000,\quad d=\sigma-t-V.
$
(A5)--(A6) 的有理平方比较给
$
 A\sqrt{1+2/d}<V,\qquad
 \frac A d\sqrt{1+1/d}<1/500.                              \tag{A7}
$
故 $v\mapsto-u\circ(\operatorname{id}+v)$，
$u=X_{p_0}-\operatorname{id}$，在 $\|v\|_t\le V$ 的闭球上自映射并收缩。
得到真实 $X_{p_0}^{-1}=\operatorname{id}+v$，且
$
 \|(X_{p_0}^{-1})'\|_t\le(1-1/500)^{-1}.
$
已付真实 $G_{p_0}'$ 在 $9/4096$ 带的界小于 $1.000000126$，而
$t+V<9/4096$。因此
$
 F_{\rm ref}:=G_{p_0}\circ X_{p_0}^{-1},\qquad
 \|F_{\rm ref}'\|_t<1.003.                                \tag{A8}
$
在实圆由 (A1) 有 $HF_{\rm ref}=L$，解析延拓使这一恒等式成立于该复带。
这不要求先证明 $L$ 或 $H$ 在某个未付的全复域上单叶。

由原 summary，$\|G_{p_0}-x-d_{\rm old}\|_{5/2048}<7.768\,10^{-11}$。
因此 $F_{\rm ref}$ 的周期位移小于 $V+7.768\,10^{-11}$，其像仍在
$H$ 的已付带内。有限 $h'$ 无常数，故
$\|H'\|\le1+\|H''\|<15.336$，进而
$
 \|L'\|_t=\|H'(F_{\rm ref})F_{\rm ref}'\|_t<17.             \tag{A9}
$
在 $r\le1/512+10^{-9}$ 带，$t-r>0.000122$；
逐模 $k^2e^{-(t-r)|k|}\le2/(t-r)^2$ 给
$\|L'''\|_r<10^{10}$。所有后续 Taylor 线必须满足其输入像位于 $t$ 带，
而不是仅引用实圆导数。

## 3. 局部 $H^{-1}$ 的具体域及一、二 Frechet 导数

本节给出 (A8) 与下面参数分解使用的同一逆分支，而不是假设全局复逆。

在 $s_H=5/2048$，原完整 summary 已有
$
 R=\|1/H'\|_{s_H}<3.432,\quad
 B=\|H''\|_{s_H+10^{-3}}<14.336.
$
令 $r_H=10^{-3}$，则 $\kappa=RBr_H<1/20$。
对任意实角 $d_*$ 和任意 $E\in\mathcal A_s$、$s\le s_H$、
$\|E\|_s\le10^{-4}$，有 $R\|E\|<r_H/2$。
R63 的同一个收缩因此唯一解出
$
 H(x+d_*+u)=H(x+d_*)+E,\qquad \|u\|_s\le r_H .
$
记此局部逆映射为 $\mathcal I(E)=x+d_*+u$。一致收缩与直接微分给
$
 D\mathcal I(E)[b]=\frac{b}{H'(\mathcal I(E))},\qquad
 D^2\mathcal I(E)[b,c]
 =-\frac{H''(\mathcal I(E))}{H'(\mathcal I(E))^3}bc .
$
因此在整个输入球上
$
 \|D\mathcal I(E)\|\le C_1:=R/(1-\kappa)<4,\qquad
 \|D^2\mathcal I(E)\|\le C_2:=BC_1^3<1000.                 \tag{A10}
$
实际上 $C_1<3.613$，保留这个余量可同时吸收后续 $J^{-1}$ 的导数。

以下所有输入均属于该球。只用粗 (A5) 即有
$\|X_{p_0}-\operatorname{id}\|_{5/2048}<2.7\,10^{-6}$。
对 $s\le1/512+10^{-9}$、$Y_\lambda=Z+\lambda e$，
$
 s+\|Y_\lambda-\operatorname{id}\|_s<t .
$
这里将较宽带的粗位移界用于较窄的 $s$；不声称 (A9) 已在整个
$5/2048$ 带成立。已付
$\|\Gamma_{p_0}-H(x+d_{\rm old})\|<2.208\,10^{-11}$，新旧
半旋转角差小于 $8.548\,10^{-12}$。因而用 (A9) 比较
$L(Y_\lambda)$ 与 $L(X_{p_0})$，再加
$\|H'\||d_*-d_{\rm old}|$，所得费用小于 $5\,10^{-5}$。
此外 $|\mu|<9\,10^{-16}$、$\|P_1\|<0.007$，而下面的参数余项、
有限 Taylor 余项和预 Newton 有限残差均远小于 $10^{-10}$。
所以全部混合输入及其线段
$
 L(Y_\lambda)+\mu P_1+\nu r_\mu-H(x+d_*),\quad
 Q_0+\mu P_1-H(x+d_*),
 \qquad 0\le\lambda,\nu\le1
$
严格位于 $10^{-4}$ 的输入球。对应 $F_{\rm ref}(Y_\lambda)$
距离 $x+d_*$ 小于 $r_H$，故局部唯一性保证
$\mathcal I(L(Y_\lambda)-H(x+d_*))=F_{\rm ref}(Y_\lambda)$。
从而 (A8) 与 (A10) 确实在同一分支上使用。

## 4. 参数增量固定标签后的准确三段分解

$\mu$ 和 $J=\operatorname{id}+w$ 均为一次选定并保存的准确 dyadic 对象。
沿真实参数线段微分时它们固定；不求 $w$ 对参数的导数。
令
$
 Q_\mu=Q_0+\mu P_1,\qquad
 r_\mu=\Gamma_{p_0+\mu}-\Gamma_{p_0}-\mu P_1 .
$
在每个固定标签 $x$，真实实参数 Taylor 给
$
 \|r_\mu\|_s
 \le|\mu|\,\|\partial_p\Gamma_{p_0}-P_1\|_s
 +\frac{\mu^2}{2}\sup_{p\in[p_0,p_0+\mu]}
                         \|\partial_p^2\Gamma_p\|_s.       \tag{A11}
$
这正是原报告的 first_parameter_source 和 whole_box_second_parameter
两项；一阶误差已包含有限 $P_1$ 不是一个有限族导数的全部费用。

下面为简洁把同一局部映射 $\mathcal I(A-H(x+d_*))$ 写成 $H^{-1}(A)$。
有准确恒等式
$
\begin{split}
 G_{p_0+\mu}-H^{-1}(Q_\mu)
={}&H^{-1}(L(X_{p_0})+\mu P_1+r_\mu)
       -H^{-1}(L(X_{p_0})+\mu P_1)\\
 &+H^{-1}(L(X_{p_0})+\mu P_1)
       -H^{-1}(L(Z)+\mu P_1)\\
 &+H^{-1}(L(Z)+\mu P_1)-H^{-1}(Q_0+\mu P_1).             \tag{A12}
\end{split}
$
第一、三行分别不超过 $C_1\|r_\mu\|$、$C_1\|\ell\|$。

中间一行沿 $Y_\lambda$ 对其函数自变量作 Frechet 微分，准确乘子为
$
 H^{-1\,\prime}(L(Y_\lambda(x))+\mu P_1(x))L'(Y_\lambda(x)).
$
$P_1$ 始终在原标签 $x$ 取值，故没有漏掉一个 $P_1'$：
这里求的是 $Y\mapsto H^{-1}(L(Y)+\mu P_1)$ 的导数，不是改变
$P_1$ 自变量后的另一个一元函数。由 (A8)、(A10)，
$
 \|\text{中间一行}\|_s
 \le [\,1.003+|\mu|C_2\|P_1\|_s\|L'\|_t\,]\|e\|_s .
                                                               \tag{A13}
$
若另用一元函数 $H^{-1}(L(y)+\mu P_1(y))$ 的导数，则还出现
$|\mu|C_1\|P_1'\|$。加上此非负项作粗预算可以，但不能据此免费把
(A12) 中的 $P_1(x)$ 改成 $P_1(Y_\lambda)$。本证明直接固定 $x$，
完全不需要这种自变量替换。

## 5. 与原 finite pre-Newton 残差及 $J^{-1}$ 的接线

原代码的 finite_quad 和 finite_composition_Taylor_fee 完整包围
$
 Q_\mu\circ J-H\circ J\circ T_{d_*}.                       \tag{A14}
$
这一事实由 (A2) 和 R100 (100.6)--(100.7) 直接展开核对。
这里没有重新选择 $a_0,\mu,w$，也没有改动已保存有限端点系数。

保存的 $w$ 在 $5/2048$ 带满足
$
 \|w\|<9\,10^{-12},\qquad \|w'\|<1.2\,10^{-9}.
$
在所有本篇使用的较窄带，和 §2 同样的收缩构造 $J^{-1}$，给
$
 C_J:=\|(J^{-1})'\|<(1-1.2\,10^{-9})^{-1}
 <1.000000002 .
$
需给它的像留出 $2\,10^{-11}$；当前到 $5/2048$ 的余量远大于此数。

设 $\rho$ 为最终 half 误差宽度，$s=\rho+\|w\|_\rho$，且
$s\le1/512+10^{-9}$。将 (A12) 先右复合 $J$，再左复合
$J^{-1}$，并对 (A14) 使用同一局部逆，得
$
\begin{split}
 \|J^{-1}G_{p_0+\mu}J-T_{d_*}\|_\rho
 \le{}&
 C_J[1.003+|\mu|C_2\|P_1\|_s\|L'\|_t]\|e\|_s\\
 &+C_J C_1\,[\epsilon_{\rm finite}
                   +\|r_\mu\|_s+\|\ell\|_s].
                                                               \tag{A15}
\end{split}
$
由于实际 $|\mu|<9\,10^{-16}$、$\|P_1\|<.007$、$\|L'\|<17$，
第一系数严格小于 $1.004$；因 $C_1<3.613$，第二系数严格小于 $4$。
即使保留额外的保守费用
$|\mu|C_1\|P_1'\|$，并用 $\|P_1'\|<15$，第一系数仍小于 $1.004$。

这说明改进只发生在中心参考坐标误差 $\|e\|$ 的传递系数。
原 finite_quad、finite_comp、firstparam、paramTaylor 和 (A4) 均保留，
仍可统一乘原粗常数 $4$。

## 6. 哪些误差用 Hardy，哪些不用

若完整有向积分已经给出同一中心流的准确分解
$
 X_{p_0}=\operatorname{id}+(C_0+D_0)+J_{\rm total}+R,
$
其中 $\|J_{\rm total}\|_{\mathcal A_\sigma}\le j$、
$\|R\|_{\sup,\sigma}\le r$，并令
$c=\|(C_0+D_0)-a_0\|_{\mathcal A_\sigma}$，则
$
 \|e\|_s\le j+c+
 \sqrt{1+\frac4{e^{2(\sigma-s)}-1}}\ r.                    \tag{A16}
$
仅真正的 sup 余项 $r$ 需要 Hardy 转换；已是 Wiener 范数的完整
$J_{\rm total}$ 与准确中心选择误差 $c$ 不再乘这个因子。
若实际账用 R86 的更紧 genuine sup source/tail，而不是 R72 的粗余项，
必须核对其与 $J_{\rm total}$ 的拆分恒等式和同一有限 $C_0+D_0$。

当前精确有限多项式没有改动；因此这是对同一个已存预 Newton 对象的新
独立误差证明，并非修改旧报告的显示数值。若实际改变有限 $C_0+D_0$
或把新的 signed $J$ 加入有限近似，则需要重新形成相应 $P_i,\mu,w$
及其完整有限残差，不能沿用本篇的对象同一性。

(A15)--(A16) 以及所有域门完整证明了 R101 所需的接合。
新 $j,r,c$ 的真实报告、R31 最终有理不等式和完整 PDE/非线性闭合，
均不由本篇替代。
