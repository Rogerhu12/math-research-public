# R165. GKZ 全迹、genus 权与原二阶行的等变维数

日期：2026-11-12。状态：**已证明的原对象比较；未证明主目标。**

[完整证明及原文页码](../notes/2026-11-12-gkz-full-class-trace-and-second-augmentation.md)。

对本课题实际
$\mathcal H_\ell=C_\ell\times U\times\Gamma$、$\Gamma=C_p$，
原点 $Q=[t_0]\operatorname{Tr}_{C_\ell U}P_\ell$ 满足
$N_\Gamma Q=0$。原 GKZ 完整类群系数已再取 $N_\Gamma$，
不能替代 $D_2=\sum_j\binom j2\tau^j$。
非基本判别式的旧导子项须保留；在实际映射下它们是
已由 $t_0$ 杀掉的基层完整迹。

GKZ（1987）Theorem C 位于
$\operatorname{Jac}(X_0(N)/w_N)$ 的 Fricke-plus 分量。
E389 的实际 $w_{389}=-1$，所以原定理的这个分量不能
被认作本曲线的原始非零行。原文的奇判别式限制也不被省略。

二次 genus character $\varepsilon$ 在奇阶 $\Gamma$ 上恒为一：
$$
 \sum_{c,v,j}\varepsilon(cv\tau^j)P_\ell^{cv\tau^j}
       =N_\Gamma\sum_{c,v}\varepsilon(cv)P_\ell^{cv}.
$$
它可改变其他二次块，不能给原二阶权。真正的阶 $p$ 字符须
保留
$$
 \sum_j(1+T)^jQ^{\tau^j}
          =N_\Gamma Q+T D_1Q+T^2D_2Q+\cdots
$$
在 $T=\zeta_p-1$ 的整展开及其格规范。

进一步，设 $k=\overline{\mathbb F}_p$、
$G=\operatorname{PSL}_2(\mathbb F_\ell)$、
$I=\ker(k[\mathbb P^1(\mathbb F_\ell)]\to k)$。
对原 $p\ge7$、$p\mid\ell+1$ 输入，
$V=I/k{\bf1}$ 不可约、维数 $\ell-1$。
原 $D_2$ 权向量 $w_2\in I\setminus k{\bf1}$，因为
其和为 $u\binom p3=0$ 而权非恒定。
若一个有限维 $kG$ 模 $W$ 和 $G$-线性映射 $L:I\to W$
满足 $L(k{\bf1})=0$、$L(w_2)\ne0$，则
$V\hookrightarrow W$，故 $\dim W\ge\ell-1$。

此界只约束以上明确等变线性假设；不排除非等变算术方法、
非线性配对或真正的指定 CM 取值论证。当前仍须为原
$\zeta_p$ 字符展开付清整格、完整 $h_Fu$ 迹及二阶原始性。
