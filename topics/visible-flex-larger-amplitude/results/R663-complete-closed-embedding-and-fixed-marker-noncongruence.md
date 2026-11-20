# R663：同一0241闭合场的完整嵌入及固定标记后的非全等

2026-11-20，Astra-larger-resume-24b2ab87-20261120。

**状态：同一准确0241候选的完整闭合相位族已证明为强C²连续嵌入；加入R661四个固定标记后，仍为嵌入且含反射的Euclidean商距离严格为正。** 全部922个原径向胞、全部角、上下反射及两帽均已覆盖，没有未付的正则盒。本条没有支付全域曲率、reach或度量目标，也没有给出求解精化收敛序列。

## 1. 准确对象与闭合接口

采用[同v5后续六步的真实终态](../notes/2026-11-20-curvature-qp-physical-h2-next-six-result.md)，bundle SHA256为

`0241f7144f82b485350f684e999c8fb3fa71c94a942339da0bfa9f00bdb30023`。

场按[R656](R656-fullclosed-continuous-geometry-with-complete-analytic-lift.md)的准确含义定义：$J=923,M=160$，自由三jet为保存的binary64对应准确有理数，节点是原FullHold的准确$\alpha_i S+\beta_i$；S、R是同一固定标量问题的准确实数，由原严格盒包围。core派生槽准确取$T_j=-2jc_j$，不把独立舍入后的槽当作新准确定义。上半场为

$$F=q+\chi(s)\bigl((R+S-s)e_r(\Theta(\phi))+H e_z\bigr).\tag{1}$$

完整解析角lift不截频。本次高度为准确有理数

$$H={8466126705245239\over4503599627370496}>1.$$

R656 Reader逐项检查原仿射接口，而非容差近似：core值、$F_s=e_z$、高度二阶jet为零，末端q的0/1/2 jet全零。每个相邻Hermite胞共用相同三jet，故径向接缝准确C²。core关于$z=0$反射的水平一阶和高度二阶匹配；末端由$\chi=1,\chi'=\chi''=0$与q三jet为零得到真实平帽的完整二阶匹配。core物理角导数$\rho=\Theta'$的连续正性由本次同源区间计算给

$$\rho\ge0.16574514795307826>0.\tag{2}$$

因此角坐标是圆周微分同胚。上下活动环带和两张真实Cartesian平盘按这些接口组成同一个闭参数球面；帽中心使用Cartesian坐标，不把极点处的极坐标退化算作浸入失败。

## 2. 全域一阶向外覆盖

新增完整执行源为 `scripts/resume_20261120/fullclosed_first_geometry_interval.py`，它只消费R656已有严格核的一阶部分，并复用原准确场定义和全角覆盖。

在每个准确径向piece，把quintic Hermite q及其径向导数升阶到6。旋转架连接项包含在角导数中；完整$\chi H$与$\chi(R+S-s)e_r(\Theta)$分别加入$X=F,V=F_s,T=F_\phi$的Bernstein控制系数后，才取径向凸包。不是先对q与lift各自取大区间再相加。角向有限多项式使用R656的严格变换、二阶余项和正oversampling折扣；$\sin(\Theta-\phi),\cos(\Theta-\phi)$使用24项Taylor及完整余项。

本次$Q=2048$，每个准确piece径向一份，利用已证对称性计算513个代表角盒，覆盖全圆而非只取513个点。设

$$N=T\times V,\qquad E=V\cdot V,\qquad W^2=N\cdot N.$$

对$W^2$同时计算$|T\times V|^2$及$E|T|^2-(V\cdot T)^2$，取两个有效区间的交。全部原胞逐一检查$E>0,W^2>0$后，计算同一个$A=\operatorname{diag}(1,1,1/4)$的实际单位法向支撑

$$S_A={AX\cdot N\over\sqrt{W^2}}.\tag{3}$$

原922胞顺序完整覆盖，零个未付盒。输出的最坏值及保守准确十进制界为：

| 全域量 | 实际向外输出 | 本文采用的准确有理界 | 最坏原胞 |
|---|---:|---:|---:|
| $E$下界 | .748271689410275 | $E\ge.74827168$ | 904 |
| $W^2$下界 | .008761092509419904 | $W^2\ge.0087610925$ | 921 |
| 活动及平帽$S_A$下界 | .3778238146070988 | $S_A\ge.37782381$ | 905 |
| $|F|^2$上界 | 4.226462839798485 | $|F|^2\le4.22646284$ | 880 |
| 完整未标记像直径上界 | 4.111672574414693 | $D_0\le4.111673$ | 由完整半径界 |

平帽的实际支撑为$H/4\ge.46996443987785896$，故不降低表内全域下界。下半场及其连续单位法向按同一水平反射取得，A与反射交换，所以全部界保持。使用的每次基本算术、平方根均作nextafter向外扩张；准确有理输入、严格三角变换与平台假设同R656，未把普通浮点采样读数冒为连续界。

## 3. 正支撑直接支付完整嵌入

这里仅用[R650](R650-positive-definite-flow-support-reach.md)第2–3节在偏移参数$u=0$的证明，不需要曲率常数。简述其完整逻辑以区分嵌入与尚未支付的reach：

对任意$x\ne0$，正定线性流$e^{\tau A}x$的每条轨道与单位球唯一相交，给光滑投影$\pi_A:\mathbb R^3\setminus\{0\}\to S^2$；其微分核为$\operatorname{span}(Ax)$。式(3)全域为正，故F不经过原点，且$AF$不在切平面中。因此$\pi_A\circ F:S^2\to S^2$是局部微分同胚。定义域紧致使它为满的有限覆盖，目标$S^2$单连通而定义域连通，故覆盖只有一层。于是F单射；紧致单射浸入是嵌入。

这没有预先借用曲面单射，也没有仅凭局部正则性排除自交。第1节的闭球拓扑与完整准确C²接口，以及第2节整面的正支撑，正是本次已付的全部输入。

R248的相位定义以绕竖轴旋转和可逆材料角重参数化生成活动部分，平帽逐材料点固定。其像是完整未标记像的绕轴旋转；A与这些旋转交换，所以正支撑和正则性对全部相位准确保持。固定光滑角微分同胚的平移作用在C²范数中连续，连同原准确接缝给全$t\in[0,1]$的强C²连续。无需抽样若干t代替此全族论证。

## 4. 四个固定p4标记仍保持全族嵌入

采用[R661](R661-complete-nonplanar-activity-and-four-fixed-markers.md)第4–5节完整参数：上帽圆心$(a,0,H),(0,a,H),(-a,0,H)$、下帽圆心$(0,0,-H)$，$a=3/20$；四个半径依次为$1/25,9/200,1/20,11/200$，高度全为$h=1/1000$。在所属帽的外法向加

$$u_i(x)=h\left(1-{|x-c_{i,xy}|^2\over b_i^2}\right)^4_+.$$

上述四张图为本次明确的准确多项式组件，没有待数值求解的参数。各支撑盘互不相交且位于$|x|\le1/5<R$内；在边界有零0/1/2 jet，因此与原帽及完整闭球准确C²相接。图的水平投影直接证明其正则性。R661对同一A且任意$H>1$已严格给

$$S_A\ge64/267>0,\qquad |\kappa|\le5.\tag{4}$$

未改活动面具有第2节的正支撑，原平帽也正；故整个带标记的闭球浸入仍有统一正支撑$\min(.37782381,64/267)>0$。再次应用第3节投影论证，所有相位都是嵌入。标记准确固定，与相位无关；强C²连续亦保持。

标记帽的固定参考度量取其自身共同诱导度量；活动部分保留原固定g，接缝平领准确一致。不声称给平盘加非零图仍保持旧平盘度量。固定握持区取上帽$|x|\le9/20$的带标记图面，具有相对内点，边界相反两点距离为$.9$。

## 5. 同一0241的非平面输入和实际非全等

不能把R661的6077系数值移用本候选。本次对0241使用已刊准确Fraction检查器，实际重新覆盖全部922胞、零失败。两条轴迹非零的共同左端有理下界为

$$a_*={562178326815370681039402279\over1237940039285380274899124224}>.4541,$$

逐胞所选非零角高度多项式的端点三jet中，最小非零绝对值为

$$z_*={2800790754697453\over144115188075855872}>.0194.$$

lift断点仍准确为节点894。R661的解析延拓、半转对称及两轴非零迹证明因此适用于本次同一0241；全部活动面没有平面开片。有限接缝不含二维开集，反射与相位重参数化保持该性质。第4节的实际嵌入现在已付，所以此结论是像上的平面胚结论，不再只是参数条件。

四个标记支撑圆半径互异，其圆心仿射独立，差向量行列式绝对值$4Ha^2>0$。[R238](R238-planar-germ-marker-rigidity.md)将平面胚补集识别为一个活动闭环带和四张闭图盘，故任何两个成员的欧氏全等必须逐个固定四个支撑圆心，只能为恒等。此证明包含$O(3)$的反射。

[R662](R662-complete-closed-C0-difference-and-inherited-size-amplitude.md)已为同一0241给完整相位见证到相位0整像的距离$L\ge.914520539$；见证在$z=0$，固定外帽图的高度绝对值至少H，故添加本标记不降低该界。第2节更紧的直径给

$$D_{\rm marked}\le D_0+2h\le4.113673,$$
$$\boxed{\delta_{\rm hold}/D_{\rm marked}>.22231,\qquad
\operatorname{diam}(H_{\rm grip})/D_{\rm marked}>.21878.}\tag{5}$$

两个像实际不同，R238的刚性遂排除其全等；其第4节的$O(3)$及有界平移紧性排除仅以刚体极限使Hausdorff距离趋零，严格得到$\delta_E>0$。这里没有给数值商距离下界；小标记的商幅度仍可很小。

## 6. 实际执行、SHA与完整复现

新完整一阶源SHA256为

`469ebec620ae325875b7cbb57662d56d094a64607ebb0f87c116029e804d9eda`。

同R656几何源SHA `2a8d09fd1c85e96a9167b705c0fe77a9107bfe935928ceb914c271ffc5c17377`；严格区间核SHA `f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d`。原节点报告SHA为 `fc52830031f1fa6ba7e00788d164cefdb88188fc35a56f8dcbab1b1b94012692`。

完整一阶报告 `continuous-0241-complete-first-geometry-q2048-r1.json` SHA为 `2bfe3a6e4371473e5b54e6b229a28facb2d9fba88e855d518287a5b780637125`，实际415.658847秒、自然退出0。非平面报告 `nonplanar-0241-complete-coefficients.json` SHA为 `3e2ab302bccd26e1f01b2c2844790cd883032e4540f1fcc8b369dda3cfd310ac`，实际.896200秒、自然退出0；其已刊源SHA `43d1ac2351def55be984113726d5a22b9d483baa715fb4f5a653b2b83173f268`。

Python3.12.14/NumPy2.3.5，单BLAS，本地执行，未造Actions run。逐胞报告只scratch；Git保完整小源、全部输入身份/参数及本紧凑结论。0241和节点报告的准确重建链见第1节链接及其中v5源/父链，不要求下载被删除的工作数组。

设`topic`为checkout内本题路径、`work`为仓库外工作路径：

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/resume_20261120/fullclosed_first_geometry_interval.py" \
 --bundle "$work/geometry_path/curvature-qp-physical-h2-next-six.npz" \
 --node-report "$work/fullclosed_solver/data/fullclosed-hold-warm.json" \
 --interval-source "$topic/scripts/parallel_20261117_arclength_interval_positive.py" \
 --geometry-source "$topic/scripts/resume_20261120/fullclosed_geometry_interval.py" \
 --angles 2048 --radial-subdivisions 1 --beta 1/4 \
 --out "$work/root/continuous-0241-complete-first-geometry-q2048-r1.json"

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/resume_20261120/fullclosed_nonplanar_coefficients.py" \
 --bundle "$work/geometry_path/curvature-qp-physical-h2-next-six.npz" \
 --node-report "$work/fullclosed_solver/data/fullclosed-hold-warm.json" \
 --out "$work/root/nonplanar-0241-complete-coefficients.json"
~~~

**剩余责任。** 当前0241全观察最大Gram误差仍约$.0240136$，远未到$10^{-6}$；全域连续metric、同一固定模型的实际精化收敛、完整活动曲率和全族$\operatorname{reach}\ge.03D$仍未支付。第3节只用正支撑证明嵌入，不能把它误写为R650完整reach定理已经触发。后继谱优化候选也不能无差界地继承本条一阶证书。
