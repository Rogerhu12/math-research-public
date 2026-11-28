# 已证明：真实截面有符号初值及其整角格余项

对象与 [CRW](R149-supplement-correlated-ray-wave-forcing-and-signed-cut-seed.md) 相同。本文给出一个独立可执行的严格初值公式。全部沿程输运与全频响应仍未随此公式付清。

## 原件与截面

固定 $c=76285779072683/320000000000000$；令 $\rho=r_*-c$，其中 $r_*$ 使用已证整区间端点。$c$ 与该根区间均在原根三次片内，程序用有理数比较片两端。Taylor 原 run 43664023495/1 的 75+205 项完整目录、native/process/publication 逐整件 SHA 已锁。按自然文件名取 $\chi$ 的全 15 阶系数、$X_\phi,T,Q_f,G,a_0,b_0$ 六场各 0–8 阶完整前缀与 9–14 各序号、$(a_1,b_1)$ 各 0–12 阶。共 70 个历史整件，逐件对 native 与 publication 的 bytes/SHA、原 source/runtime/algebra/manifest 核验。16 个原双圆盘 majorant 用 run 43676926141/1 的整件及 process/publication 准入。完整 76 条自然输入的本地只读身份核对为 2606796 B。历史 SHA 是 a3d84d905ce72e3a854874bbe98d119623f3f8de，精确路径和三个来源散列在 seed_admission 源内。没有重算原 Taylor 系数或原 majorant。

给定实际某场完整径向前缀至 $N$，外半径 $R$、外角条带半宽 $\sigma$ 及原全模上界 $M$，令 $t=\sup|\rho|/R<1$。在实角上径向 $p$ 次、角向 $q$ 次的余项不超过
$$
 M\frac{q!}{\sigma^q R^p}\left(\frac{d}{dt}\right)^p
     \frac{t^{N+1}}{1-t}.
$$
先在任意较小两半径用 Cauchy 公式，令半径趋于其原界，得到第 $n$ 径向系数 $q$ 次角导不超过 $M q!/(R^n\sigma^q)$；逐项求和得式。截面初值取 $p=0$，保留 $\rho$ 的整个原区间。根解析延拓半径只用于这个真实同片点的余项。

## 有符号角网与完整每格输出

取一物理周期 $P=\pi/2$，$N_g=2048$，中心 $kP/N_g$，对每中心同时保存中心与整个相邻半格宽 $h=\pi/(4N_g)$ 的复矩形。有限系数以球算术 Horner 在整个 $\rho$ 上求值。对角导 $q$，每一原非圆周 Fourier 系数先乘 $(4ij)^q$，然后累加进 $j\bmod N_g$ 桶，用逆 DFT 并乘 $N_g$。在这些节点，原指数与桶指数完全相同，故即使有高频别名，全部原系数都属于准确点值。每个节点再加上述解析余项。

所需导数若到 $m$，实际算节点至 $m+3$，并由完整 Fourier 和与同阶解析余项求出 $m+4$ 阶全实角上界 $B$。对于 $q\le m$，把节点处 $q$ 至 $m+3$ 阶的有符号 Taylor 式在 $[-h,h]$ 直接作区间运算，再向实、虚部各加 $B h^{m+4-q}/(m+4-q)!$。积分型 Taylor 余项保证对整个格和每个已保留导数成立。该操作没有给纯 DFT 插值误差赋予导数。$\chi,T$ 至 9 阶、$X_\phi$ 至 8 阶，$Q_f,G,a_0,b_0,a_1,b_1$ 至 6 阶；$p_\sigma$ 和 $R_\sigma$ 分别至 8、6 阶。所有数据均为物理角、所有阶数均为实际导数除阶乘。

逐中心与逐全格直接保留 $s=\sqrt{-T}$、$\omega=2(-T)^{3/2}/3$、$P^c_\sigma-\phi=\chi-\sigma\omega$、$p_\sigma=X_\phi-\sigma\omega_\phi$、$G p_\sigma^2$、$C=G(-T)^{-1/4}$。$C$ 恒为径向标量，另核前六角导含零。所需正实幂由 $f y'=\alpha f'y$ 的真实 Taylor 递推给出；每个 $f_0$ 在全格有正下界。两射线的 $Gp_\sigma^2=a_0+i\sigma s b_{0,+}$ 用原两独立有符号包围核相交。原 native 证明同一个复 $\delta$ 的负频分支满足 $a_{1,-}=-a_{1,+}$、$b_{1,-}=b_{1,+}$。因此输出四组
$$
 R_{\sigma,\epsilon}(c,\phi)=
 \frac{\epsilon a_{1,+}+i\epsilon\sigma s\, b_{1,+}}{G p_\sigma^2}.
$$
实几何量取实投影，有符号复振幅两部均保留。每个最终球用向外端点存 binary64 四元组（实低高、虚低高），全流 gzip 后完整读取检测 shape、EOF、有限性、全格 $T<0$ 和 $\omega,p_\pm,v_{0,\pm}>0$，再记整件 gzip SHA。大输出留 job 私盘。入口脚本为 fourfold_codazzi_true_characteristic_seed_owner.py；root_input 与 seed_admission 为其两个直接模块。三个模块/原代数的精确 SHA、全部参数与新 run/结果须在消费时核对。本证明只建立新截面计算规则，不登记尚未执行的新数值门或整件输出。
