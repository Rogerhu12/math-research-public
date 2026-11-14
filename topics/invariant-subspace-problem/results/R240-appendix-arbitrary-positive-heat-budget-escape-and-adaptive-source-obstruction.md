# R240 附录：任意正热锚的平方预算逃逸、正常取值消失与自适应真源障碍

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf；根代理核验非单调量词、实际头与纯尾的统一误差及状态锚。

状态：完整证明。旧[可数正热乘积](R240-appendix-countable-positive-first-semigroup-products.md)处理非负系数累加的单调情形。本稿允许每一步任意重新选择非负 $\ell^2$ 行，证明其平方预算逃逸仍迫实际热算子弱趋零，并将其与真正常见证的统一源成本相接。不涉及非正系数或额外标量重标定。

## 1. 实际正热族与主结论

对任意非负实 $b\in\ell^2$，记
$$
R(b)=e^{-X_b}\in A',\qquad \|R(b)\|\le1.
$$
全部对象均为原实际第一阶与其真实收缩半群。
非负时间已经吸收到 $b$ 中。
已有有限因子分解给
$$
R(b+d)=R(b)R(d)\qquad(b,d\ge0,\ b,d\in\ell^2).
\tag{1.1}
$$
本文只在有界有限头与原完整尾之间使用它，不假设变动行具有任何单调性。

**定理1.1。** 对每个固定正常泛函 $\phi$，
$$
\boxed{
\lim_{L\to\infty}
\sup_{\substack{b\ge0,\ b\in\ell^2\\\|b\|_2\ge L}}
|\phi(R(b))|=0.
}
\tag{1.2}
$$
特别，对任意选择的正行序列，
$$
\boxed{
\|b^{(p)}\|_2\to\infty
\quad\Longrightarrow\quad
R(b^{(p)})\to0\ \mathrm{WOT}.
}
\tag{1.3}
$$
没有逐坐标收敛、嵌套支撑或累加假设。

## 2. 一个位的大系数已有统一衰减

令 $D_j^0=I-2E_j$ 为纯位 Cayley 主项。
原实际 $V_j$ 与 $D_j^0$ 都增生，且
$$
\|V_j-D_j^0\|\le8\eta_j,\qquad
0<\eta_j\le e^{-770\,16^j}.
$$
纯单个位准确有
$$
e^{-D_j^0}=e^{-1}(I+2E_j),\qquad
\|e^{-D_j^0}\|=e^{-1}(1+\sqrt2)<0.889.
$$
两收缩半群之间的有界 Duhamel 式给
$$
\|e^{-V_j}-e^{-D_j^0}\|\le8\eta_j.
$$
故对全部 $j$，
$$
\|e^{-V_j}\|<0.9.
$$
任意 $x\ge0$ 分为整数与不足一的余时段，得到
$$
\|e^{-xV_j}\|\le0.9^{\lfloor x\rfloor}.
\tag{2.1}
$$

若某个 $b_j>M$，从 (1.1) 抽出该位，
其余实际因子仍收缩，因此
$$
\boxed{
\sup_jb_j>M
\quad\Longrightarrow\quad
\|R(b)\|\le0.9^{\lfloor M\rfloor}.
}
\tag{2.2}
$$
不要求大系数所在的物理位固定。

## 3. 系数一致有界时，完整头截断误差一致可付

现在固定 $M<\infty$，假设
$$
0\le b_j\le M.
$$
对整数 $m\ge1$，令 $V_j^{[m]}$ 为
[R230 完整头矩稿](R230-appendix-first-walsh-observability-and-canonical-positive-head-moments.md)
在前 $m$ 个物理位构造的真实有限头 Cayley 元。
它们两两交换并增生，且
$$
\|V_j-V_j^{[m]}\|
\le18\theta_{j,m},\qquad
\theta_{j,m}=\prod_{\ell=j}^{m-1}\eta_\ell
\le\eta_{m-1}
\quad(j<m).
\tag{3.1}
$$

记
$$
H_m(b)=\sum_{j<m}b_jV_j^{[m]},\qquad
Q_m(b)=e^{-H_m(b)}\otimes R^0(b_{\ge m}),
\tag{3.2}
$$
其中 $R^0$ 是纯独立正一阶的收缩半群，
第一个因子仅在前 $m$ 位作用。
两个因子均收缩，所以 $\|Q_m(b)\|\le1$。

实际有限头 $\sum_{j<m}b_jV_j$ 与 $H_m(b)$
都为有界增生算子。
因此有界 Duhamel 式与 (3.1) 给
$$
\left\|
e^{-\sum_{j<m}b_jV_j}-e^{-H_m(b)}
\right\|
\le18Mm\eta_{m-1}.
\tag{3.3}
$$
实际正尾与纯正尾之间，旧热乘积稿 §3 已支付
$$
\|R(b_{\ge m})-R^0(b_{\ge m})\|
\le8M\sum_{j\ge m}\eta_j.
\tag{3.4}
$$
它先在有限系数上用两个收缩指数的 Duhamel 式，
再取已识别的强极限，因此没有遗漏原无界域。

把实际热分为实际头与实际尾，再分别应用
(3.3)--(3.4)，得到
$$
\boxed{
\|R(b)-Q_m(b)\|\le M\varepsilon_m,
\qquad
\varepsilon_m=
18m\eta_{m-1}+8\sum_{j\ge m}\eta_j\to0.
}
\tag{3.5}
$$
这一估计在所有 $b$ 满足 $\|b\|_\infty\le M$ 时一致。
乘积差只用各因子收缩性；不要求实际头与纯尾混合交换。

## 4. 纯尾真空系数与任意正常泛函

令 $\Pi_m$ 为前 $m$ 位的有限 Walsh 柱投影，即尾部取真空。
对于任意正常泛函 $\phi$，置
$$
\phi_m(T)=\phi(\Pi_mT\Pi_m),\qquad
\tau=\|\phi\|,\qquad
\epsilon_{\phi,m}=\|\phi-\phi_m\|\to0.
\tag{4.1}
$$
最后的收敛是迹类密度的双侧有限秩压缩收敛，
不是对任意无界弱逼近使用正常连续性。
并有 $\|\phi_m\|\le\tau$。

纯尾的准确真空系数为
$$
r_m(b)=
\langle R^0(b_{\ge m})1,1\rangle
=\prod_{j\ge m}e^{-b_j}(1+b_j).
\tag{4.2}
$$
它由有限张量截断取强极限得到。
对固定 $b\in\ell^2_+$，
$\sum_j[b_j-\log(1+b_j)]<\infty$，故该乘积有意义。

当 $0\le b_j\le M$ 时，
$$
x-\log(1+x)=\int_0^x\frac{u}{1+u}\,du
\ge\frac{x^2}{2(1+M)}.
$$
从而
$$
0<r_m(b)
\le
\exp\!\left[-\frac{\|b_{\ge m}\|_2^2}{2(1+M)}\right].
\tag{4.3}
$$
$\phi_m$ 仅观测尾真空，
$e^{-H_m(b)}$ 又收缩，所以
$$
|\phi_m(Q_m(b))|\le\tau r_m(b).
$$
结合 (3.5)、(4.1)，得到具体且统一的正常取值估计
$$
\boxed{
|\phi(R(b))|
\le
\epsilon_{\phi,m}
+\tau M\varepsilon_m
+\tau\exp\!\left[
-\frac{(\|b\|_2^2-mM^2)_+}{2(1+M)}
\right]
\quad(\|b\|_\infty\le M).
}
\tag{4.4}
$$
这里保留全部实际头 carry 和该正常泛函的真实尾误差。

## 5. 预算逃逸及保持状态值所需的界

给定任意 $\epsilon>0$。
先固定足够大的 $M$，使
$\tau\,0.9^{\lfloor M\rfloor}<\epsilon$；
这由 (2.2) 控制全部 $\|b\|_\infty>M$ 的行。

对其余行，在固定 $M$ 后取足够大的 $m$，
使 (4.4) 的前两项之和小于 $\epsilon/2$。
最后取足够大的 $L$，
使 $\|b\|_2\ge L$ 时第三项小于 $\epsilon/2$。
这就是 (1.2)。
对所有秩一正常泛函应用 (1.2)，便得到 (1.3)。

因此有以下真实非零状态锚结论。
对任意固定正常 $\phi$ 及 $\epsilon_0>0$，
若
$$
|\phi(R(b^{(p)}))|\ge\epsilon_0
$$
对全部充分大的 $p$ 成立，则
$$
\boxed{\sup_p\|b^{(p)}\|_2<\infty}
\tag{5.1}
$$
（有限多个初项不影响此式）。
更一般，可用固定 $F\in B(H)$ 的
$|\phi(R(b^{(p)})F)|\ge\epsilon_0$ 代替：
$T\mapsto\phi(TF)$ 仍为固定正常泛函，故同样证明。

若整列 $R(b^{(p)})$ 弱收敛于一个非零算子，
可选择一个在该极限上非零的固定秩一泛函，
所以该序列的平方预算也必有界。
若只取一个非零弱聚点，则结论相应只用于收敛到该聚点的子列。
这里只给必要条件，不将有界预算等同于强收敛。

## 6. 与真见证的自适应源预算合并

现在令 $\phi$ 来自一个固定非零正正常慢湮灭见证。
取[R150 实际矩负权判据](R150-appendix-actual-normal-moments-negative-occupation-criterion-and-witness-divergence.md)
及其统一预算节中的实际有限头代表 $v_p$。
有限秩时也可取该稿已识别的完整实际擦除源 $\widetilde v_p$。

该统一预算结论给：对每个固定 $R<\infty$，
$$
\inf_{\substack{b\ge0\\\|b\|_2\le R}}
\|e^{-X_b}v_p\|\longrightarrow\infty.
\tag{6.1}
$$
它是该稿时间 $1/2$ 的结论在 $a=2b$ 后的准确重标记。

如果随头选择的实际正热因子 $R(b^{(p)})$ 同时满足
$$
\sup_p\|R(b^{(p)})v_p\|<\infty
$$
和一个固定非零状态锚
$$
|\phi(R(b^{(p)})F)|\ge\epsilon_0>0
\quad\text{对全部充分大的 }p,
\tag{6.2}
$$
其中 $F$ 固定，则 (5.1) 使 $\|b^{(p)}\|_2$ 一致有界，
与 (6.1) 矛盾。
故这样的族不存在。
同样结论适用于 $\widetilde v_p$。

等价地，任何把这条真实源序列压成有界族的正热选择，
其有效系数预算必趋于无穷，
于是热因子本身弱趋于零；
它在每个固定正常泛函、每个固定有界右因子上的取值都趋零。
这不是只对某一个固定热锚的排除。

本节只讨论已定义的真实头代表或明确擦除源。
它不把有界源成本推广为任意未知重构表的成本，
不排除非正系数、额外发散标量重标定或其他交换子正则器。
也没有由这项正热方法边界得出普通 Hilbert ISP 的完成结论。
