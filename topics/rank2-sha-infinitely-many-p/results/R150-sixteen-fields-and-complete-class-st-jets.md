# R150 — 十六个独立固定域的完整类群 ST 非零 jet

**状态：已证明。日期：2026-11-12。**

固定 $E=389\mathrm a1$。取基本判别式
$$
 -7,-11,-19,-67,-20,-24,-35,-52,
 -187,-232,-267,-372,-483,-555,-795,-1435.
$$
它们平方类秩 16，389 全部分裂，类数只为 1、2、4，类群
指数均为二。所有断言及实际分歧理想基由纯整数 reduced-form
[证书脚本](../scripts/check-sixteen-exponent-two-heegner-fields.py) 完整核验。

对每个域，以选定的分歧理想基构造固定
$\Phi_D=\sum_{d\mid D_0}\pi\circ d_d$。基的各 lift 在每个
素于 $D_0$ 的环类群中真为阶二，并同构映到整个最大阶类群。
故 $\Phi_D(z_c)$ 正是全部 $h_D$ 项之和，且微分唯一 q 首项
证明它非恒定。固定整数 $t_0$ 杀掉全部基层扭迹后，
$\Psi_D=[t_0]\Phi_D$ 在有限个原 CM 中心都取 O。

为每个域给出显式 principal ordinary 素数 q。Cornut 的
**平凡完整 class+tame 角色**、ST 的真实挠点识别和原始 Gauss
求和，给 $\log_E\Psi_D$ 的指定 tame $-1$ Mellin 分支非零。
原始整数投影 $q-N_n$ 与准确两个初层递推排除所有全迹扭。
因此存在同一个固定 $C,m_0$，使全部源中心的
$h_{D,c,m}=m![v^m]\log_E\Psi_D(t_c(v))$ 在
$C\mid m,m\ge m_0$ 时非零；统一高度为 $O(m\log m)$。

取固定 B 吸收 C、阈值和全部有限局部条件。对
$\ell\equiv-1\pmod B$、$\ell+1=pu$、$u\le U$、
$x/(\log x)^2<\ell\le x$，只删
$O(U^2\log(U+2)/\log x)$ 个 $\ell$，十六个域的**实际完整**
原点
$$
 Q_D=[t_0]\operatorname{Tr}_{F_D[\ell]/L_D}P[\ell]
$$
同时非扭，且 $v_\ell\log_E Q_D=1/p$、
$\widehat h(Q_D)\ll u^2\log\ell$。若大因子 $p>x^{0.667}$，
则高度为 $o(p)$，故实际 Q 不被 p 整除，并有 Gauss 半层界。

[完整证明](../notes/2026-11-12-sixteen-fixed-fields-and-complete-class-st-jets.md)
保留所有类群项、原 $U$ 迹、固定映射、共同系数进程和全尾界。
全部 p 在十六域都惰性的同余类密度为 $2^{-16}$；它与大因子
筛的联合删除由 R149 单独证明，本结果不以密度直接相交。

完整证明 §7 已将 R149 的正筛余量、R138 的目标例外删除和
本文全部首 jet 坏集在**同一组输入**上合并：存在表中一个
固定 $F_*$ 和无穷多个 p，使 p 普通、非异常并在 $F_*$ 分裂，
原 $Q$ 非扭、$NQ=0$、$\widehat h(Q)=o(p)$，且 $a_\ell$ 为
p 单位、$u\ll p^{333/667}$。范数一簇 Sha 有限，原指数
$a\le(p-3)/2$，长度上界为 $2(a+1)$。
同一实际点的 $a\le1$ 仍未证，故尚未完成主目标。
