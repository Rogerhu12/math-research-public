# R675：新弓形端度量的无穷小内帽倾斜与中央弯曲矩

2026-11-28。针对 [R673](R673-thick-bowed-tilted-endpoint-metric-with-strict-intrinsic-chord-slack.md) 的**一个已固定的非旋转度量** $g_+=F_0^*g_{\rm eucl}$，下面给出任意无穷小内帽 $y$ 倾斜必须由真实弓形中央段支付的标量矩。此条件属于完整一阶等距方程，适用于未预设能积分为有限等距族的无穷小解。相应[公开输入](../notes/2026-11-28-r675-bowed-endpoint-pose-response-scope.md)求包括全部空间列的实际应变响应及此矩，并将独立细网的误差与有限子空间距离分别记录。

## 一阶 Gauss 关系与转动场

记端点浸入为 $F=F_0$。若 $V$ 满足 $\delta g_{ij}=F_i\cdot V_j+V_i\cdot F_j=0$，则在每一点有唯一无穷小转动 $Y$ 使 $V_i=Y\times F_i$（将两个一阶列的纤维内积保持延拓到有向正交标架即可）。混合导数相等给 $Y_i\times F_j=Y_j\times F_i$，故两个 $Y_i$ 均切于面。在局部正交单位基 $P,U=n\times P$ 中写两切向导数为 $Y_1=aP+bU,Y_2=cP+dU$，则该等式还给 $a+d=0$。第二基本形式的一阶变化准确为
$$
 \delta b_{ij}=n\cdot(Y_i\times F_j).
$$
在上述点的正交坐标，$\delta b_{11}=-b,\delta b_{12}=a,\delta b_{22}=c$。$Y$ 的混合二阶导的法向差为零，即 $a b_{12}+b b_{22}-c b_{11}-d b_{12}=0$，由此得
$$
 b_{22}\delta b_{11}-2b_{12}\delta b_{12}+b_{11}\delta b_{22}=0.    \tag{1}
$$
可在点取法向坐标把切框系数导数的法向分量直接写成上述二基项；原一般材料坐标由双线性变换得到相同的行列式导数等式。$V$ 只有 $C^2$ 时，混合二阶导 $Y$ 按分布使用，连续的一阶量使结果仍逐点成立。原分段节点由连续性延拓。

## 正 $y$ 母线处的准确矩

沿 $\varphi=\pi/2$，令 $k=H'(r)$，$v=R_y(\omega)e_x$，$b_0=R_y(\omega)e_z$。两个物理坐标向量为 $F_r=e_y+k e_z,~F_\varphi/r=-v$。未归一法向
$$
 N=b_0-k\cos\omega\,e_y,\qquad n=N/|N|.
$$
本节的 $b_{ij}$ 始终指材料基 $(\partial_r,r^{-1}\partial_\varphi)$ 上的双线性分量，基可以不正交。直接取实际 $F_{rr},F_{r\varphi}/r,F_{\varphi\varphi}/r^2$ 的法向值得
$$
 (b_{ij})=\frac1{|N|}\begin{pmatrix}H''\cos\omega&\omega'\\
                      \omega'&k\cos\omega/r\end{pmatrix}.
$$
由 $Y_r\cdot N=0$ 有 $Y_r\cdot b_0=k\cos\omega\,Y_r\cdot e_y$；又 $(-v)\times N=e_y+k\cos\omega\,b_0$，故
$$
 \delta b_{12}=n\cdot(Y_r\times(-v))=|N|\,\partial_r(Y\cdot e_y).
$$
外刚帽固定时 $Y(b)=0$；单位内帽 $y$ 倾斜及任意内平移给 $Y(a)=e_y$。将 (1) 与此式合并，弓外 $H'=H''=0$ 而 $\omega'\ne0$ 于开区间，因而
$$
 \boxed{-1=\int_l^u\frac{\cos\omega}{2\omega' |N|}
   \left[\frac{H'}r\,\delta b_{11}+H''\,\delta b_{22}\right]dr .}    \tag{2}
$$
没有在平接圈除以消失的 $\omega'$；积分区间为 $\omega'=-M/r$ 的真实中央平台。没有弓时右端为零，解释了旧饱和材料线在一阶上的扭转消失。有弓时，(2) 留有真实响应通道，其可解程度需由完整场决定。

具体地 $\int_l^u|H'|=2A$、$\int_l^u r|H''|=4r_0\max|H'|$，后式来自 $|H''|$ 的中点反射以及 $H'$ 的一正一负两个单峰。对单位倾角
$$
 \max_{[l,u]}\{ |\delta b_{11}|,|\delta b_{22}|\}
 \ge {2M\over 2A+4r_0\max|H'|}>6.6.
$$
用 $A=.0036,r_0=.1475$, $\max|H'|<3.44A/.081$ 与 $M>.36/1.1$ 即得。这个下界是每单位弧度的二基响应，并非有限形状本身的主曲率值。

## 全三张应变与真正二阶条件

采用同一外刚框，真实角率一阶提升 $V_{\rm pose}=r(\omega/\vartheta)e_y\times R_y(\omega)e_r$，内端单位 $y$ 倾斜、外端为零且两阶 jets 匹配。未知包含两个自由内平移和其余双端齐次的完整 Cartesian 场。端几何关于 $y\mapsto-y$ 对称，$e_y$ 作为无穷小转轴在此反射下保持，因此任一满足此驱动的完整线性解与其反射平均后给反射解。对该驱动求 $V_x,V_z$ 的全部余弦列和 $V_y$ 的全部正弦列，不会漏掉一个只能靠破坏该反射才能完成的线性内转角。反对称零驱动核的二阶分岔是另一个问题。

若同一准确路径还二阶可微于真实内倾角，令 $Z$ 是加速度，则 $\delta g(Z)+2dV^TdV=0$。内端准确二阶刚姿含 $r(e_y\times)^2R_y(\vartheta)e_r$，自由二阶内平移同样保留。实际有限输入仅在独立网格一阶完整应变与中央矩都接近所需值时复用同一完整分解求此方程，随后用准确二阶刚帽姿态评价一个真实非零角增量的度量，不把形式 Taylor 系数称作实等距族。单位角驱动一阶失败也不排除开头角速度为零的更高阶分支。

[R679](R679-elliptic-sign-separates-material-reflections-of-any-nonplanar-flat-rim-annulus.md) 已严格排除固定 $g_+$ 下正、负反射两端的整体连接。本响应只检验已知正端附近的同支、非镜像新目标；局部线性或二阶结果不再用来推进向负反射端。
