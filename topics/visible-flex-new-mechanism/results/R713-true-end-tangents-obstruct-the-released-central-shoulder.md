# R713　释放五厘米真平片后，原两端切向仍排除全幅肩

**已证明。** 在 [R704](R704-two-controlled-developable-shoulders-and-exact-central-window.md) 的中央恒截面内，将近端从 $x=.38$ 移到 $x=.33$，释放原主片中的 $.05$ 真平段、原长 $.001$ 的水平座和 [R686](R686-framed-annular-window-and-curl-to-actual-metric-transfer.md) 全部三次弯转。远端取第三转末、首次进入真竖壁之处。保留原两边开带的真实刚姿及同一源度量时，曲率上界 $K=10.4$ 已排除所有 $.60\le\lambda\le1$。结论允许 [R697](R697-free-axial-crown-translation-and-curl-only-window.md) 任意实轴移 $\sigma$。这次排除用的是材料弦两端的**有向切线**，对任意光滑等距填充成立。未启动此五厘米输入的数值工作流。

## 材料直线的方向预算

设 $c:[0,L]\longrightarrow\mathbb R^3$ 为单位速 $C^2$ 曲线，$|c''|\le K$，取单位向量 $V$。记两端沿同一材料行进方向的切线与 $V$ 夹角为 $a,b\in[0,\pi]$。$c'$ 在单位球上的行程给 $\angle(c'(s),V)\ge a-Ks$ 及 $\angle(c'(s),V)\ge b-K(L-s)$。若 $L\ge(a+b)/K$，在近端前 $a/K$、远端末 $b/K$ 两不相交区间分别积分余弦界，中段取 $c'\cdot V\le1$，得

$$
 V\cdot[c(L)-c(0)]\le L-\frac{a+b-\sin a-\sin b}{K}.                 \tag{1}
$$

固定材料直线若在源开发坐标中为单位速测地线，则任一 $C^2$ 等距像上的空间加速度恰为法曲率乘单位法向量。主曲率绝对值上界 $K$ 因而足以使用 (1)，内部是否选用 [R708](R708-finite-central-shoulder-continuation-with-all-six-physical-controls.md) 的六个控制并无影响。

## 原源、真实端姿和矛盾

取 $d=.20,\alpha=.016$，$T_0=(0,\cos\alpha,\sin\alpha)$，$E_2=(0,-\sin\alpha,\cos\alpha)$。共同平移 $h_\lambda$ 不影响弦。在源的开发图 $(u,z)$ 中，固定直线 $z=-.19$ 从 $x=.33$ 横跨三转至竖壁开邻域的接点。其原纵标 $v=z-\zeta\sin\alpha$ 全程满足 $|v|<.196<.203$，因为真实截面 $0<\zeta<.326$。投影速度 $b_0=(\cos^2\theta+\cos^2\alpha\sin^2\theta)^{1/2}$ 介于 $\cos\alpha$ 和 $1$，其中 $\theta$ 是原截弧切角。故

$$
 .470 < \cos\alpha\,\big(.051+.25\pi/3+.101\pi/2\big)
 \le L\le .051+.25\pi/3+.101\pi/2<.472 .                              \tag{2}
$$

近端切确为 $e_x$，因上片绕过 $d e_Z$ 的 $x$ 平行轴转 $\lambda$。远端切确为 $-E_2$，因原末段垂直向下，投影到 $T_0^\perp$ 后正得此方向，冠只刚移。选 $V=E_2$，则 $a=\pi/2,b=\pi$。$3\pi/(2K)<.454<L$ 保证两端积分区间互不相交。由 (1)–(2) 得严格上界

$$
        E_2\cdot[c(L)-c(0)] < .472-\frac{3\pi/2-1}{10.4}<.116.          \tag{3}
$$

另一方面近端在源的位置为 $.33e_x+d e_Z+v_-T_0$，其中 $v_-=z-d\sin\alpha<-.19$。相位 $\lambda$ 时改为 $.33e_x+d e_Z+v_-(T_0\cos\lambda+E_2\sin\lambda)$。远端的位置从源只加 $\sigma e_x$（及已经去掉的共同平移）。R686 给其高度 $\zeta_f>.2229$。原末点在 $E_2$ 上相对 $d e_Z$ 的投影恰为 $(\zeta_f-d)\cos\alpha$。由此真实弦满足

$$
 E_2\cdot[c(L)-c(0)]=(\zeta_f-d)\cos\alpha-v_-\sin\lambda
 > .022+.19\sin\lambda .                                               \tag{4}
$$

在 $[.60,1]$ 上 $\sin\lambda\ge\sin(.60)>.56$，所以 (4) 大于 $.1284$，与 (3) 矛盾。即使把曲率门改成半径 $.096$ 单独给出的必要界 $K=1/.096$，(3) 仍严格小于 $.116$。证明直接使用同一真实材料路径和两个物理开带，未将有限离散弦、数值续解失败或局部逆函数的大小当成障碍。

更一般地，在两端转角和同一个 $z$ 及两端高度保持不变的扩长设计上，若当前开发长度仍满足 (1) 的互不相交条件，则全幅 $\lambda=1$ 必须有 $L>(3\pi/2-1)/10.4+.022+.19\sin1>.538$。移动端点本身、改变真实平肩的放开范围或重新设计源截线，会改变其他方向的必要预算。这里未改变远端竖壁、证成其他长度的候选或解决中央窗两条纵端及整闭面问题。
