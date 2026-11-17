# β=.75 真前缀的固定弧长规范化候选

**数值证据，仍为带边前缀。** 对已接受 β=.75 父的同一 common-jet quintic 定义一个新映射；固定目标度量不变。M112、构造角网2048，独立读出角网4096/每径向胞4分点，509胞共8,343,552点的实际 relative Gram 最大值为 **6.39303335385e−7**；父场在同样本为2.50493133921e−6。本条不冒闭面、全t、reach或固定参数精化收敛。

## 一个明确的新映射

原有限 Fourier 场记 F(s,φ)，q=|Fφ|。F 是按父mesh、保存的0/1jet及同源 JVP二jet构成的唯一逐胞五次式。固定N=2048，令q_N为q在该网格上的实三角插值（Nyquist按单cos项处理），b(s)=mean(q_N)，λ=a/b，c=(0,0,zmean)。以同一个核心ρ定义Θ(φ)=∫₀^φρ。新坐标ψ由

$$\int_0^{\psi(s,\phi)}q_N(s,u)\,du=b(s)\Theta(\phi)$$

确定，映射为 $\widetilde F=c+\lambda(F(s,\psi)-c)$。只要q_N>0、ρ>0，这是一一圆周重参数。目标仍是原 $g=ds^2+a(s)^2\rho(\phi)^2d\phi^2$，没有从新像重新定义目标g。

有限角谱使 Fssφ 存在且跨径向节点连续；因此q、q_N及b在s方向C²。上述正性条件下，隐函数ψ与新映射均C²；原共享0/1/2jet通过同一变换保持共享。一般抽象joint C²函数不自动具有这里使用的Fssφ，本构造使用有限角谱这一额外性质。

令m=b′/b，B_N为q_s,N−m q_N的零基点周期原函数，则ψ_s=−B_N/q_N。程序使用实际五次式导数，完整保留

$$\widetilde F_s=\lambda F_s+(1-\lambda)c_s+\lambda'(F-c)+\lambda F_\phi\psi_s.$$

读出网格加密不改变构造N。程序真正计算角误差 $|F_\phi|^2/q_N^2-1$、混合误差 $\widetilde F_s\cdot F_\phi/q_N$ 和径向误差 $|\widetilde F_s|^2-1$；没有把角项强置0。样本以旧φ参数覆盖新圆周，报告的角位置因此注明parent_angle。

曲率在同像的 $G=c+\lambda(F-c)$ 上计算，其λ′、λ″及中心二jet全部来自相同原函数；角重参数不改变主曲率。它避免数值反解ψ二阶，却没有省掉空间映射的二jet。

## 实际读数与范围

最大Gram在s=.997、旧角2.65378676304：rr=4.53200089234e−7，角项−1.33e−15，混合项3.44929596060e−7。全样本rr/角/混合项最大绝对值为5.73845716e−7/4.31e−14/4.99936177e−7。

主曲率最大6.28899872326，位置s=.969625、旧角1.37137882437。最大|λ−1|6.213e−13、|λ′|4.716e−10、|λ″|1.976e−6；按旧角对应的像点距离最大8.970e−13、径向速度变化6.505e−7。核心0/1jet变化为0，二jet变化2.34e−16。此距离只计中心缩放后的对应像点，不是共同材料点的位移；后者还含ψ重参数。极小像点距离解释了为何实际像和曲率几乎保持，而同g的角向误差显著下降。

q_N样本最小.165992486156；利用每个采样s处的角Fourier导数l1界，所有角的Lipschitz下界至少.152117677822。**全径向正性尚未在本轮作连续包围**；C²结论仍明示以上正性条件。径向极值、曲率、Gram均为采样读数，无interval证书，不把单层audit加密当作README第5项同解的网格/频率/t收敛。新候选不等于原有限Frenet方程又一次接受，原BVP源及状态未改。

## 复现与身份

本地运行；S为本题scripts目录，raw仅scratch。

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH="$S" python "$S/parallel_20261117_prefix_arclength_readout.py" --input parallel-model-inward-svd-b075.json.gz --construction-angles 2048 --angles 4096 --radial-subdivisions 4 --out parallel-model-inward-b075-arclength-c2048-a4096.json
```

- 父SHA256：`852a673f4464090f003fd44c3247a819cf9bae0418d07caf97f8edb0e3d39471`。
- 源SHA256：`0ad4400b648cfd2937b58c59a811c3a2cdb30af68e3b3c3e261091e097dbdaf2`。
- 实际输出SHA256：`0009aa0d2f29cf0204751e6a68bea887dab54dffb14b75af1b03fbd7d5fe8b5e`。

后续8192角/8分点必须沿同构造N2048；若改变构造N，另记为另一候选。将此算子用于已有C²桥时，桥两侧须统一使用同N/同目标ρ/同基点规范，不能只改一侧而声称原六jet仍相同。

## 同一候选的独立读出加密

固定原父、common-quintic和构造N2048，仅audit从4096角/4分点升到8192角/8分点。509胞共33,366,016点：最大Gram仍为 `6.393033353852322e−7`；κmax变为 `6.289016378306884`（s=.96965625）。全样本rr/角/混合项最大绝对值 `5.88445908e−7/4.685e−14/5.13978062e−7`。同源像点匹配差上界样本 `8.972e−13`，不解释为固定材料点位移。核心二jet差 `2.347e−16`。

命令沿原源，把 `--angles 8192 --radial-subdivisions 8`，输出 `parallel-model-inward-b075-arclength-c2048-a8192.json`；SHA256 `09291b8e5f98d8394a2a9eff814ddd24822f89903e139505ec8b84f554feb306`。这是固定候选的读出加密，不是README第5项重新求解后网格/频率/t精化收敛。

后续[R638](../results/R638-global-positive-arclength-coordinates-for-two-prefixes.md)已严格结清本文留下的全径向/全角正性条件；原Gram/曲率采样证据不因此升级为连续误差或嵌入证明。
