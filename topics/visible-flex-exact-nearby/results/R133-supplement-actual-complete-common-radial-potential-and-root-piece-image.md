# R133 补篇：真实全频共同径向势及完整根片坐标覆盖

2026-11-15，visible-exact / phase_inverse。

**状态：公开 Actions 的新标量计算已完成，16门全部通过。**
本篇记录同一固定 intrinsic 参数 $\eta_0$、原完整65中心和193方向族的共同径向势
$V,V_T,V_{TT}$、全部所用分母及坐标像的实际界。
最大实际复径向半径为 $H=1/6000$。
其中 $H=1/10000$ 和 $H=1/6000$ 的共同坐标逆像，确实覆盖原真实根片2549；
另外两个较小半径的整片覆盖标志仍为 false。

本结论没有给完整 reference 两列、正侧选定图、旧圆 $H_V$ 逆、
全高 BVP 逆或真实 PDE 分支。新的参考势不会把原 free-Airy
source 上界变成一个可相减的误差。

## A. 实际运行、精确输入与规则

实际作业为
[43685624307/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43685624307)。
workflow event 与实际科学 checkout 都是
1ca03990aed2531717528d8f51d1156138f1988a。
科学子进程退出码为0，实际数学时间为
0.15750965700001984秒，父进程记录的子进程 wall time 为
0.4651510470000062秒。

本次只运行新的完整标量球代数。原 target、FFT、真实根点导数、
intrinsic 0--15阶、已存 characteristic 0--14阶及原 Fourier 多项式
均未重新计算，原文件也未改写。20件科学输入的实际来源为：
17件固定公开历史 blob、2件当前精确新文本、1件当前字节相同的原代数源码。
完整输入收据的 canonical SHA256 是
441a6d12da4bf98ce729059094267ee869549efe653fb0b2d081959a56b62d2b。

可执行入口：

- [科学源码](../scripts/fourfold_codazzi_common_radial_potential_budget.py)，
  30953 bytes，SHA256
  042713687b7d2d561ba25678a76ae9dbd95e042ec1d57bf4a0caa89310063fe7；
- [20件精确输入及参数](../notes/2026-11-15-R133-common-radial-potential-budget-CI-inputs.json)，
  11519 bytes，SHA256
  44555290b424807278c933aaa5cc26c8a8e198ef1ff02ebdc7728c4ad6810437；
- [公开 worker](../scripts/fourfold_codazzi_common_radial_potential_budget_public_worker.py)，
  17311 bytes，SHA256
  f67fa3f9b63834715d0aa7711bee2e836979c55dacd3c83055c09dfd035e2cd0；
- workflow 为 .github/workflows/visible-exact-common-radial-potential-budget.yml，
  SHA256
  6fab4a579d018cfb7e6cba6d5213d54e10600cd7a93cf22b78626dace56428eb。

CLI 为 --repo、--manifest、--manifest-sha、--out-dir；
全部数值输入先恢复到 runner 的独立临时科学树，再核每件 bytes/SHA256。
历史读取固定在 a3d84d905ce72e3a854874bbe98d119623f3f8de，
不是从正在变化的 working tree 推断原对象。
Python 3.12.14、python-flint 0.9.0、NumPy 2.3.5、SciPy 1.17.0
及320-bit Arb 与声明完全一致；两件 Python 的完整 immutable AST 检查实际通过。

runner 在 06:29:28.400079 UTC 与 06:29:34.635130 UTC
分别真实 pull；两次根 README 与课题 README 差异都为空，
所得提交均为上述实际科学提交。
本次按
[当前不保存可重算数据的规则](../notes/2026-11-15-R133-reviewed-public-CI-rules-reproducible-data.json)
执行：没有新 artifact、Release 或数据文件进入 Git。
保存的是脚本、参数和下面的小结论、执行身份。

## B. 本次确实覆盖的数学对象

使用
[最小完整势预算](R133-supplement-minimal-complete-common-radial-potential-and-derivative-budget.md)
中的 $x=r-r_*$，故旧 $\rho=-x$、$K=xk$。
完整背景仍保两个修补均值、65中心及193方向的全部有限 Fourier 槽，
复参数乘积是 bilinear 乘积，不以共轭或 real-part 操作替代。

实际参数域为
$$
 |\Re\delta|,\ |\Im\delta|\le10^{-8},\qquad
 |\Re z|,\ |\Im z|\le\frac1{9409}.
 \tag{A.1}
$$
对真实 Fourier 标签取 $z=j^{-2}$，所有 $|j|\ge97$、两个 carrier
符号和物理频率 $n=4|j|$ 同时被覆盖。
$z=0$ 是无限频率极限，始终不是物理 even mean。

径向域是以同一个已证真实根为中心的复圆盘 $|x|\le H$。
原完整 intrinsic 三阶证书所在的复矩形包含真实根区间加
$R_C=1/2000$ 圆盘；本次重新核的是这个精确包含门。
原0--15阶数据与完整三阶复域按 B.2--B.5 支付新增所需4、5阶尾，
不重算任何已成点导数。

参考量保持准确抵消：
$$
 \eta=-\gamma\langle v\rangle,\qquad
 \overline A=\frac32\int_0^1s^{1/2}(\eta\sqrt k)(sx)\,ds,\qquad
 \kappa=\eta\sqrt k\,\overline A^{-1/3}.
 \tag{A.2}
$$
原 characteristic 系数0--8直接读原完整 background stage；
9--14逐件读原成功 append-only stage。
它们的原 source、manifest、runtime、payload 与 publication
身份均分别核对，未把原阶段改标为新源码。

采用原 $c$ 的 $\eta_r/\eta$ 抵消式以及同一 $W$：
$$
 V=\frac{W}{\kappa^2},\qquad
 V_T=\frac{W_r-2\ell W}{\kappa^3},\qquad
 V_{TT}=\frac{W_{rr}-5\ell W_r+(6\ell^2-2\ell_r)W}{\kappa^4},
 \quad \ell=\frac{\kappa_r}{\kappa}.
 \tag{A.3}
$$
所有有序积及真实径向导数先按准确公式合并，再取完整模上界；
没有用两个旧上界之差代替残差。

支持域 $R=3/8000$ 实际通过，给
$$
 \sup|(\eta\sqrt k)^{(3)}|\le82901951.5,\qquad
 \Re k>56.818053533268,\qquad
 \Re\eta>1.253478692369.
 \tag{A.4}
$$
因此备用支持半径 $1/4000$ 无需执行；这不是一个失败域。

## C. 四个实际复径向域的完整势界

下表为实际返回值向上取整后的便读界；原小结论保留更锐的球。
所有界都在 (A.1) 的完整复参数盒和相应 $|x|\le H$ 上成立。

| $H$ | $\sup|V|<$ | $\sup|V_T|<$ | $\sup|V_{TT}|<$ |
|---|---:|---:|---:|
| $9/10^6$ |245|21973|2929766|
| $1/20000$ |252|22902|3100660|
| $1/10000$ |261|24237|3358536|
| $1/6000$ |276|26431|3830956|

最大域实际原界分别为
$$
 \sup|V|\le275.19610691070556640625,\qquad
 \sup|V_T|\le26430.5394287109375,\qquad
 \sup|V_{TT}|\le3830955.76953125.
 \tag{A.5}
$$
同一最大域还给 $\sup|c|<30.071462$、
$\sup|\kappa|<4.622270$、$\sup|W|<5492.144501$。

这里是完整频率参数的势界，未在 $j=97$ 作有限拟合后外推。
完整 primitive 的中间分母统一满足
$$
 |1-\ell_{\rm mode}^2z|\ge\frac{193}{9409}
 \quad(1\le\ell_{\rm mode}\le96).
 \tag{A.6}
$$
最大域的其余实际门可向下取为
$$
 \Re k>58.645596177262,\quad
 \Re\eta>1.253612341566,\quad
 \Re\overline A>9.649140207891,\quad
 |\kappa|>4.485249802470,\quad
 |1+\theta|>0.999998241662.
 \tag{A.7}
$$
这里 $\theta=z\alpha/\eta$ 是同一 mode-dependent 参考系数，
不是旧角向 drift 的替代记号。原 holomorphic 分支由正实部门固定，
没有借复参数上的实能量不等式。

## D. 共同坐标像与真实整根片

令 $T_*(0)=0$、$(T_*)_r=\kappa$。
已核的完整相对导数门给圆盘像包含；最大域有
$$
 \sup\left|\frac{\kappa}{\kappa_*}-1\right|
 <0.021232015105<1,\qquad
 D\!\left(0,0.000742956050168040\right)
       \subset T_*(D(0,1/6000)).
 \tag{A.8}
$$
这是原完整复参数盒上同一 common radial coordinate 的实际单叶门。
逆像比较再消费原已成 old-product fold 上界，保原
$|\Im\phi|\le3/128$，不把实际角域换成冻结径向线。

| $H$ | 保证的 $T_*$ 像半径下界 | 保证的旧 $|\rho|$ 半径下界 | 原整根片覆盖 |
|---|---:|---:|---|
| $9/10^6$ |$4.094411222093\times10^{-5}$|$4.412122179694\times10^{-6}$|false|
| $1/20000$ |$2.262985125010\times10^{-4}$|$2.438584284963\times10^{-5}$|false|
| $1/10000$ |$4.497042989340\times10^{-4}$|$4.845996662290\times10^{-5}$|true|
| $1/6000$ |$7.429560501680\times10^{-4}$|$8.006066537225\times10^{-5}$|true|

准确原根片最坏覆盖半径为
$$
 h_*=\frac{893368603925465506687}
 {21990232555520000000000000}.
 \tag{A.9}
$$
最后两行的 true 是实际程序直接比较完整下界与这个有理数的结果。
前两行 false 予以保留，没有把局部成功写成整片成功。

物理身份仍只在原 piece2549 上成立。辅助 root-cubic 延拓虽然给
更宽的数学参考域，但它不会把 piece2548、2550 或新2547、2551
认作相同物理背景。那些实际 piece 的系数差、非零入口、
原 seam 以及原独立 mean 继续按各自已付合同处理。

## E. 完整两源变换与 gauge

取共同参考 gauge $G_r/G=B-c$、$G(r_*)=1$。
最大域给如下向上圆整的实际界：
$$
 |G|,\ |G^{-1}|<1.005055,\qquad
 |G_r|<30.405703,\qquad |G_{rr}|<5475.738444.
 \tag{A.10}
$$
原共同参考两源系统仍是
$$
 U_T=P+\frac{g_2}{\kappa G},\qquad
 P_T=(n^2T-V)U+\frac{A_jg_1+c g_2}{\kappa^2G}.
 \tag{A.11}
$$
它实际给
$$
 \left|\frac1{\kappa G}\right|<0.224081,\quad
 \left|\frac{A_j}{n\kappa^2G}\right|<0.062640222,\quad
 \left|\frac c{\kappa^2G}\right|<1.502350.
 \tag{A.12}
$$
两个普通源独立保留，未使用 $g_{2,r}$。
这些是相应系数的点态/复域界，尚未自动变成整个 positive
Green 或所有径向 source-to-port 的积分算子常数。

## F. 可复核小证据与准确范围

已保存的实际小结论是
[actual-result.md](../notes/common_radial_potential_budget_ci/run-43685624307-1/actual-result.md)，
13866 bytes，SHA256
844b88e24c7922d0ea8ca14520b5d40eb7f0f9c811d04030099d3ca05964cf6c；
完整小执行记录是
[execution.json](../notes/common_radial_potential_budget_ci/run-43685624307-1/execution.json)，
27645 bytes，SHA256
d4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9。

原科学 process 在 runner 临时目录为16990 bytes，SHA256
ec9f4e61493e4f3c24530a5c7163d98f2bf2a741fbd3569ffa1bbf881df94e23；
临时完整 native 为6607 bytes，SHA256
eb2b1323b0c01497ceddf28abac6223b41ad2c313055bce3428076bea0148ee1。
它们没有作为新的可重算数据另行保存。
小执行记录只保留身份、参数、16个真实门和必要最终势/gap/image/source结论；
signed 中间证书始终只在临时 native 中。

16门包括原完整运行/复矩形/两个修补均值身份、全部原特征系数9--14的
逐件复用、原 whole-product fold 身份、支持域成功、四case的真实
完整分母/像门，以及物理 even mean 和 reference seam 独立性的范围门。
没有用一个 aggregate success 代替其中失败的数学门。

后续构造应使用本次实际支付的 $V$、两个 $T$ 导数和共同像域，
建立参考方程的真正两列及其 root/positive/old-circle 接口。
本篇本身仍明确保留这些未付项；同样保留原两个 carrier 分支、
物理 even mean、真实 piecewise seam 和 full head--high feedback。
