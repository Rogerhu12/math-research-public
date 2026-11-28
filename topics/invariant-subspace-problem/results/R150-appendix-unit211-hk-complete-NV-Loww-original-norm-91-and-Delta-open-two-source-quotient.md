# R150 补充：HK 完整 NV–Loww 的原范数、纯权返回与 Delta 余图恢复

日期：2026-11-28。会话：Astra-ISP-8542378f-20261127。

## 1. 本次实际结果

同一未完成输入经两处 JSON 类型修复后，唯一正常运行 run46161292265 / job141028973573 已完整成功：**8.428479614 秒，峰值 92588 KiB，内层 exit 0**。完整三维乘法、三个伴随坐标、全多项式 lift，以及全部八个两原式系数均返回。得到总次数 $91$ 的非零纯权必要式；没有执行其 QQ 因式分解或与旧核的 QQ gcd。

记本次最终保留的纯权多项式为 $P(\lambda,u,Q)$。其精确定义是下文固定三维乘法的 Norm、实际两原乘子共同因子取消，以及只剥旧已付支持；不是从显示次数猜测的多项式。

| 实际对象 | 次数 $(\lambda,u,Q)$ | 总次数 | 项数 | 规范字节 | SHA256 |
|---|---:|---:|---:|---:|---|
| 原有理 Norm 的分子 | $(84,21,13)$ | $108$ | $8786$ | $416530$ | 90ed1e1e0eaa8de135772d7ef5ca4e8181298eda80892712746332fa5d15e1f0 |
| 原有理 Norm 的分母 | $(77,3,4)$ | $83$ | $1292$ | $54276$ | 52aa1bfbc458de9144637b0c86b8bae8d278d0c9ec39e4aeb116da54579d0f34 |
| 取消实际乘子共同因子后的标量 $C_{\rm sc}$ | $(96,25,13)$ | $122$ | $13201$ | $694463$ | 34a6a816a71cd37ac3bb18fc73b13a2cc9d3d9d4918face119275ace002786f5 |
| 最终保留 $P$ | $(72,19,9)$ | $91$ | $6447$ | $274332$ | 1b7bedb75aa5004944a36238ebda660aa85fdd77e683583e2a84612eb17b327e |

上述规范字节只记录定义的长度及 SHA，没有存储或传送对应系数载荷。全部分母均已逐项通过旧单位检查。

源码完整返回同一个原 $t$ 上的身份
$$
\Omega_*(t)NV(t)+\Theta_*Loww(t)=U_{\rm paid}P(\lambda,u,Q)t^3.
\tag{1}
$$
$U_{\rm paid}$ 是明确的旧权单位。再用同源的 $t$ 多项式逆，得到 $P$ 本身的完整原两源组合。因此每个当前原点都令 $P=0$。

在已独立关闭整 $\Delta=0$ 的当前余图中，NV 唯一恢复 $t$；本篇还证明这两式的商精确同构于对应的纯权商 $(P)$。这只描述完整 NV 与 Loww 的两式理想，全部原均值、个别 N/P 和其它条件仍需同时满足。

单一新权关系不单独给有限权点或排空；三维原权支撑仍须与其它已刊原核同点相交。

## 2. 原图与完整两源

使用已刊正确 $h=k$ 图的
$$
A=2\lambda^2-2\lambda+1,\quad B=4\lambda^3-6\lambda^2+3\lambda-1,
\quad \delta=1-Q,
$$
$$
\xi=B/A,\quad \ell=A^3/B^2,\quad T=A^2/B,\quad
h=k=1+\xi,\quad w=\lambda-1-T.
\tag{2}
$$
令 $\mathcal A$ 为三参数 QQ 权环在
$$
ABQ\delta P_fMP_{02}\lambda(2\lambda-1),\qquad M=4bc\delta
\tag{3}
$$
的实际纯权分子支持处的局部化。所有原有理系数分母均由这些既有单位支付。本次算法没有倒 $\Delta,T_{\rm num}$、Loww 的三次头或新 Norm。

原恢复为
$$
f(t)=-\frac{P_c+bcQ\Phi t}{P_f},\quad
V(t)=\frac{Jf-G+bcQt}{Q},\quad
W_1(t)=\frac{T_0+4uf}{2},
$$
$$
x=\frac{(u-\ell Q)V-(u-\ell)W_1}{M},\qquad
y=\frac{\ell W_1-uV}{M}.
\tag{4}
$$
所有符号都沿正确 f33 原坐标定义。完整原值
$$
NV=N_Ff+bcQS\xi\,t+N_C,\quad
N_F=(3-4\lambda)Q+J\xi(\xi+3-2\lambda),
$$
$$
N_C=(\xi+3-2\lambda)(-G\xi+Qwu),\qquad
S=2\xi+3-2\lambda
$$
满足已刊完整原返回
$$
QN_4((1,w,h,h))=2NV.
\tag{5}
$$
记
$$
\Delta=\Phi N_F-S\xi P_f,\qquad T_{\rm num}=P_fN_C-P_cN_F.
$$
本次同一 $t$ 的原式是
$$
P_fNV=T_{\rm num}-bcQ\Delta\,t.
\tag{6}
$$
完整 Loww 是
$$
L(t):=2P_{02}(2\lambda-1)w
-bct[K_w+4(f-u)(t-2)],
$$
$$
K_w=2[t^2+(5u-4x-2)t+2(x^2-\delta y^2)
+4x+4\delta y-4ux+2u^2-6u+Q].
\tag{7}
$$
它的准确原来源为
$$
L=NS-PS+E_{W2},\qquad
E_{W2}=b(2p-u-X)E_B+c(2q-u-Y)E_C.
\tag{8}
$$
自由 $f$ 修正和全部原 N/P 值项保留。旧 Loww/E1、Loww/EBo 两个资源触界目标没有执行。

原 (5)、(8) 的准确依据分别为
[四个完整个别 N/P 返回](R150-appendix-unit211-h-equals-k-corrected-individual-NP-NV-scalar-returns.md)
及
[旧 Loww 已成范围与冻结回执](../notes/2026-11-28-unit211-hk-original-low-weighted-two-projections-resource-boundary-8542.json)。

## 3. 原 t 逆与首一三维环境

由 (4)，$L$ 对 $t$ 至多三次，且
$$
c_0=L(0)=2P_{02}(2\lambda-1)w
=-\frac{2P_{02}\lambda^2(2\lambda-1)^2}{B}
\tag{9}
$$
在 (3) 中为单位。令
$$
v(t)=-\frac{L(t)-c_0}{c_0t}.
$$
这是真多项式，并已实际完整返回
$$
tv-1=-L/c_0.
\tag{10}
$$
因此 $t$ 在两源商中已有原多项式逆，不要求增加一个未付几何局部化。

置 $\zeta=1/t$，定义
$$
q(\zeta)=\zeta^3L(1/\zeta)/c_0
=\zeta^3+q_2\zeta^2+q_1\zeta+q_0.
\tag{11}
$$
$\mathcal A[\zeta]/(q)$ 是完整首一三次环境；所有系数下降、$q_0=0$ 及其它头零都保留。它只是计算原必要式的多项式环境，不是整个原系统的充分模型。

反转 (6) 得
$$
a(\zeta)=\alpha+\beta\zeta,\qquad
\alpha=-bcQ\Delta,\quad \beta=T_{\rm num}.
\tag{12}
$$
在本次三维运算中，两者均未反演。

## 4. 真正乘法、伴随与原两源回返

本次对 $1,\zeta,\zeta^2$ 三列分别作首一短除，完整保除法商：
$$
a\zeta^j=M_{\bullet j}\cdot(1,\zeta,\zeta^2)+Q_jq.
$$
所得矩阵为
$$
M=\begin{pmatrix}
\alpha&0&-\beta q_0\\
\beta&\alpha&-\beta q_1\\
0&\beta&\alpha-\beta q_2
\end{pmatrix}.
$$
新标量
$$
N=\det M=\alpha^3-\alpha^2\beta q_2+\alpha\beta^2q_1-\beta^3q_0
\tag{13}
$$
和第一伴随列按真实二阶余子式构造，三坐标全部乘回。令该列对应的多项式为
$$
b(\zeta)=\alpha^2-\alpha\beta q_2+\beta^2q_1
+(-\alpha\beta+\beta^2q_2)\zeta+\beta^2\zeta^2.
$$
本次进一步返回完整多项式身份
$$
a(\zeta)b(\zeta)-\beta^3q(\zeta)=N.
\tag{14}
$$
代回 $t$ 并乘 $t^3$，得到
$$
P_ft^2b(1/t)NV-\frac{\beta^3}{c_0}L=N t^3.
\tag{15}
$$
全部原 $t$ 系数实际回返，未借不同根或不同原点。

令 $d$ 为 (15) 两实际乘子及 $N$ 的旧权分母 LCM；每个分母都逐项检查为 (3) 支持。清分母后，取两乘子的全部系数与标量的共同多项式因子 $g$，逐项精除并重新对完整原两式返回。再写
$$
dN=g\,U_{\rm paid}P.
\tag{16}
$$
就得到实际 (1)。一般论证不把 $g$ 当成单位；来源是取消后的真实乘子，因此其零集未被删除。没有从未支付的原方程或矩阵头中除去公共因子。

本次实际 $g=Q^2$：它是一项、次数 $(0,0,2)$、规范 15 字节，SHA256 为 4bdbb1ded65397f7f2832cfbe27a1897b45069ed278ad90b59619c8edb008641；已用这一单项参数的规范序列精确匹配该 SHA，未重算任何原目标。$C_{\rm sc}$ 的已付剥除记录为 Q、$P_f$、M 各一层 gcd；“一层”只指源码返回的一次 gcd 商，不误称整个标签多项式恰为一次幂。各层均精除乘回。

由 (10) 和
$$
1-(1-L/c_0)^3
=L\left(\frac3{c_0}-\frac{3L}{c_0^2}+\frac{L^2}{c_0^3}\right)
$$
可直接给出
$$
P=\frac{v^3\Omega_*}{U_{\rm paid}}NV+
\left[
\frac{v^3\Theta_*}{U_{\rm paid}}
+P\left(\frac3{c_0}-\frac{3L}{c_0^2}+\frac{L^2}{c_0^3}\right)
\right]L.
\tag{17}
$$
(17) 是实际已返 (1)、(10) 的明确有限乘法表达式；它不要求展开高次来源缓存。本次没有保存或冒称展开该高次证书。

## 5. Delta 余图的精确两式商

[整正确 $\Delta=0$ 原排除](R150-appendix-unit211-hk-corrected-entire-Delta-zero-finite-DVR-original-exclusion.md)
已独立完成。只在这个当前余图，令 $\mathcal A_\Delta=\mathcal A[\Delta^{-1}]$；此时 $\alpha$ 是单位。

由 (6)，NV 精确消去
$$
t=-\beta/\alpha=\frac{T_{\rm num}}{bcQ\Delta}.
\tag{18}
$$
由 (11)、(13)，有纯参数恒等式
$$
N=\frac{\alpha^3}{c_0}L(-\beta/\alpha).
\tag{19}
$$
所以
$$
\mathcal A_\Delta[t]/(NV,L)
\simeq \mathcal A_\Delta/(N).
\tag{20}
$$
注意这一步没有预设 $\beta$ 为单位。

(17) 给 $P\in(NV,L)$，经 (18) 收缩得 $P\in(N)$。另一方面，(16) 给 $N\in(P)$，因为 $d$ 是旧单位而 $g$ 为权多项式。因此
$$
(P)=(N)\quad\text{in }\mathcal A_\Delta,
\qquad
\mathcal A_\Delta[t]/(NV,L)
\simeq\mathcal A_\Delta/(P).
\tag{21}
$$
不必另付 $g$ 或计算其因式，(21) 直接来自两个原理想包含。

在 (21) 的商内，$\beta$ 也自动是单位；显式地，
$$
\beta\,
\frac{\alpha^2q_2-\alpha\beta q_1+\beta^2q_0}{\alpha^3}=1.
\tag{22}
$$
这与 (18)、原 $t$ 单位相容，是同原两式的推论，不是未经处理便丢弃 $T_{\rm num}=0$。

全部原系统只在 (21) 上继续加入其它必要方程。两式相容不意味着其它原均值或个别 N/P 条件已经满足。

## 6. 固定权纤维与已有曲线包络

在当前 $\Delta\ne0$ 余图，(18) 使 $t$ 唯一，(4) 使 $f,V$ 唯一，(2) 使 $h=k,w$ 唯一。完整有序规范 Gram 的剩余符号由
$$
\rho^2=\delta,\qquad
p=1+\rho,\quad q=1-\rho,\quad
b=\ell/2+\rho(u-\ell)/(2\delta),\quad c=\ell/2-\rho(u-\ell)/(2\delta)
$$
及原恢复确定。对每个固定允许复权点，必要纤维是
$$
\mathbb C[\rho]/(\rho^2-\delta)
$$
的商；$\delta\ne0$ 使该二次代数约化。因此此处明列的比值/Gram 纤维长度至多二且约化。进一步原等式或几何开条件只能删去 Artin 分量。

这是对固定权的相对结论。原独立尺度 $U_0$ 的三次关系另计，未包含在上述二元符号纤维中，也没有计未经列出的矩阵轨道。

[既有曲线包络与相对六生成](R150-appendix-unit211-hk-corrected-weight-curve-envelope-8184-and-relative-six-generators.md)
给权支撑维数至多一。当前还须满足同一个 $P=0$；在完整处理它与包络的共同分量之前，不能推出原权支撑零维、有限点数或全空。

## 7. 实际身份、工程修复与未做事项

实际源为 abd714718e1915f2df3fa3f7808d7684adbc3b12，10014 字节，SHA256
039f4dd37cbe91d03c12465c62b637f177fee7bf227b39e9335833ddd3f52fda。

- run46161292265 / job141028973573，内层 exit 0。
- source commit 与实际 pull 后均为 e9083c90000316e09cd6efda8cae908bd5bf0bb3。
- pull UTC 2026-11-28T15:42:56.814966+00:00；两份规则未变。
- driver 8.428479614 秒，峰值 92588 KiB；数学最后完整记录 8.380279010 秒。
- 原同 t/逆 t 记录在 0.109575909 秒，三维 Norm/伴随/full lift 在 3.048834840 秒，完整两源取消返回在 8.181843581 秒。
- 实际 3 次首一除法、3 真乘法列、3 伴随坐标、341 次权精除、29 个已付分母检查、8 个完整两原源系数返回。
- stdout 3226 字节，SHA256 为 f010006f85337de10e92161a22abd1365c3c56a20e7c5279f9cbcd755f379843。

原预算为 180 秒 / 4 GiB，外层 195 秒；没有增加资源。

源
[完整 NV–Loww 新原返回](../notes/2026-11-28-unit211-hk-full-NV-Loww-inverse-t-monic-three-original-norm-8542.py)
只读正确 f33 的 4540 字节参数定义，完整源 SHA2ea618c508489fedffdec7418cc153f6fc213ef46b329f8c55743be312d9faa2，
前缀 SHAa56e54b840cc323675394f96484c99658cad9a8420933cd2f344fe2df0d76efc。
旧五行、旧 individual 标量、旧两固定 Loww 投影都没有执行。

第一次 e9bd/run46159596374 的 fmpz JSON 类型错误保持原记录；只修 pp 指数/次数的 Python int 转换，数学、参数定义、断言与原预算均不改变。本次新结果以实际正常返回为准，不用先前 traceback 推测未输出参数。

[本次小执行回执](../notes/2026-11-28-unit211-hk-full-NV-Loww-inverse-t-monic-three-original-norm-8542-execution.json)
只保原输出摘要、定义/次数/SHA和实际记录，不保存可重算系数或矩阵缓存。全部新权支持仍按其完整零集保留。
