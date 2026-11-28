# R762 — 正弧长坐标、双坐标物理场及原四路完整实验

Astra-larger-e4e2a2bf-20261126；实际准备记录2026-11-28 UTC。承接 [R760完整初曲面](../results/R760-cartesian-cap-join-initial-global-reach-and-exact-active-ends.md) 与 [R762完整证明](../results/R762-positive-meridian-arclength-and-two-coordinate-crown-fields.md)。仍未达到课题完成标准。本次启动四个完整物理拟合及两个独立换坐标测量，不把坐标变化当作几何改善。

## 已支付的准确数学内容及其范围

同一R760初始闭球、同一目标张量、同一材料握持区和 $0\le\theta\le.90$。两帽宽环带以 $v_-=.82(1-.0075),v_+=1-.007$ 及 $z=(v-v_-)/(v_+-v_-)$ 表示。真实先验场的速度 $r=|F_v|$、弧长 $\ell=\int r$、总长 $L$，连同
$$
 A=\frac{F_s\cdot F_v}{r}-\ell_s,\qquad
 Q^2=|F_s|^2-\frac{(F_s\cdot F_v)^2}{r^2}
$$
满足准确恒等式 $g=Q^2ds^2+(d\ell+A\,ds)^2$。固定两端的横向重参数化要使全部三项与目标相同，必须且在正确弧长坐标下足够地同时匹配 $L,A,Q^2$。总长比给真实谱误差下界 $|L^2/L_0^2-1|$；真实首末弦只给其相应必要下界。单独修平 $g_{vv}$ 不付剩余两项。

实际程序使用正的周期/径向C²样条代理 $a_\theta,a_0$。令 $\omega=0$ 于两开护领、内部为1，$b=\int\omega a_\theta/\int\omega a_0$，
$G=(1-\omega)a_\theta+\omega b a_0$。两正原函数总积分准确相等，隐式
$\int_0^{\Phi}a_\theta=\int_0^zG$ 给一一正向的C²微分同胚。角/径两个变量的全部六jet均由隐式求导得到；真实原场通过完整链式法则合成。护领内与零相位逐字返回恒等坐标，因而零相位物理初场不受代理误差影响。每一真实样条单元的积分按自身多项式系数完整计算，隐式逆以原52步有括号Newton求解。

此微分同胚保持该输入的整个像、真实曲率、嵌入性与reach；它不能将坏几何变厚，代理总长比也不冒充真实连续障碍。改形来自另加的三向物理向量场，随后独立重新计算真实Gram、曲率与support。

两个窗口各保原Fourier/径向/15个Cartesian函数，并增加真正二维周期三次局部张量积场。三层 $(n_s,n_r)=(6,3),(12,6),(24,12)$；最细两个窗口合计720个标量局部列，每列有三独立物理分量。三次基C²、精化mask $(1,4,6,4,1)/8$，可对紧支撑C²场作真正空间精化。R760原额外整帽平移列没有保留，故本搜索空间不宣称包含R760的全部原自由度；原帽SE(3)注册仍保。外袖在free_end选项跨中央末端.30与整个签名卷，在outer_locked选项保相应外部锁定，两者都在距帽圈.0062处结束，距圈.007及内碗护领仍固定。

## 原完整科学预算

四条独立路径为 outer_locked/free_end 各配 side $-1,+1$；每条均运行三层和七原相位 $0,.15,.30,.45,.60,.75,.90$，并对相同实际系数作六中间相位检查。每侧覆盖中央半面、end、cap、cap-normal与真实Cartesian碗芯五图，合计两侧构成九张物理图；不拿两侧不同拟合当已共同满足一个完整闭面结论。

| 层 | 角基础节点 | 横向区间 | 积分阶 | Fourier/径向阶 | nonlinear/inner预算 | 独立角/径网格 |
| --- | ---: | ---: | ---: | --- | --- | --- |
| 0 | 24 | 6 | 16 | 2/2 | 12/12 | 64/12 |
| 1 | 40 | 9 | 24 | 3/3 | 20/16 | 96/18 |
| 2 | 64 | 12 | 32 | 5/4 | 30/20 | 144/26 |

所有原特征点与其真实材料位置仍加到网格；五图全部三项相对Gram误差、谱误差、相对面积、最大主曲率绝对值和最小support各自返回。原真实24²帽刚体注册、16条完整帽径向路径价格及旧/新Cartesian尖点Hessian比较继续。稀疏矩阵按每批160物理点建立全六jet，前向与真转置作用于全部三向变量；稀疏保存不削减物理点或列数。

每个sign另独立测量三层各13相位共39行换坐标前后真实Gram11/12/22、原材料vv相对价、$\Phi_v$极值、开护领坐标/几何六jet、原函数总积分差与代理长度比。这两份gauge-only报告与四份真实物理拟合、一个总索引各自完整发表；原系数与可重算raw按根§15留runner。

## 冻结源、公开执行与可复现身份

全部12件Python输入由公开Actions的实际trigger提交冻结至runner独立目录。README读取提交与科学源提交分列；两次bootstrap sync及每2700秒实际 git pull --rebase 后仅读双README差异并检查最新规则。原source不随观察pull变化。Python3.12、NumPy2.2.6、SciPy1.15.3，各进程BLAS线程1；四条完整拟合并行运行，原355分钟作业上限不当成功条件，不因阶段失败削预算。

| 文件 | bytes | 全文SHA256 | Git blob |
| --- | ---: | --- | --- |
| scripts/resume_20261126/r740_rolled_disk_seed.py | 10834 | `b812afa381e2775433710edb9cfa9bd54f0b1b892935c21f2f785675bb4d866f` | `72ef28649a33d115ef9a646a581f61dc3f3ddece` |
| scripts/resume_20261126/r742_tilted_disk_two_jets.py | 9706 | `5088d1e5183b91f78d8fd1af056bd774ce6ef54b5c578277c3dc7ef04fe183bd` | `eacaa69d88eae15963aee90d948391abfb9c745a` |
| scripts/resume_20261126/r744_extruded_closed_two_jets.py | 10327 | `35bb8a1612dd22a8e215a7682ead0c9836b26f3a6c6b525a876fff178a3d6c24` | `729efd888029dbaf9953617edfde81c0c7394fdd` |
| scripts/resume_20261126/r754_coherent_mirror_bowed_walls_two_jets.py | 9754 | `aedac63cfc0ecab05108b7d1d8ea62d5fcc0ee48e3a60c09c6fe7214e829eb96` | `0f20d4a812f5f3c32526277548fc641b75864ddd` |
| scripts/resume_20261126/r756_return_elbows_preloaded_exact_rolls.py | 8933 | `39e166b6482078f39dc8bd2ee360a7a42ec02650145c85f5ebd78d7e32ec5a38` | `3daf3aa1a455c8886cd7dd92ab2f3ff0f541883d` |
| scripts/resume_20261126/publish_r734_exact_conclusion.py | 10589 | `a18fb8ef978c8220c5fa918ed25b348ac35b3d2b24758324bf73d51351a0b4dc` | `c07d8a51f944dbacddabd127522d673174498839` |
| scripts/resume_20261126/r758_curved_outer_collars_and_fixed_elliptical_crowns.py | 6352 | `54554808a73d93149a297a7302093d0afcd0b8d433b2d119223a2a2792ff40bf` | `c88481deaffb78453316a31bd6e607ca774226ab` |
| scripts/resume_20261126/r760_cartesian_curved_crown_and_lower_rate_walls.py | 10422 | `a20f2ee98d901cadb6290edbbb8ad1f8a52d5b6035e6507c171ddea93febf919` | `ec2e06753824f38d3c8ace40a8cf4deec0e51f23` |
| scripts/resume_20261126/solve_r760_curved_crown_middle_annuli.py | 20834 | `0e1e4d9f76221c43938b3c839c95f8ad51e487df1edf52b952d6f913cba2ed72` | `1bb5c19e45cc7e6e6b306309f5cae91a9875e346` |
| scripts/resume_20261126/r762_positive_meridian_arclength_and_full_jets.py | 6926 | `070aac69ce2f04c6916f730fb6a16b38a524c19ec739c5cc79ab4d39c4d5db3b` | `b19cbad376603353b8cf70bd4343466a71efd46c` |
| scripts/resume_20261126/solve_r762_gauged_crown_tensor_annuli.py | 23531 | `168547cd6db101ef575db2aaf6dcf48217577a2558c170049aa6129766afe147` | `d7f7e8878c594b02923f44c28490ff7604e4d2fe` |
| scripts/resume_20261126/run_r762_all_gauged_crown_fits.py | 11578 | `3f37d3f6a0de82a398a0a6efbd80e9cfc89361bad553767c00912b94e0fe45e2` | `6cc8acdfe90f4d4ef731263a55cf70fca5adf842` |
| .github/workflows/visible-larger-r762-gauged-crown-physical-fits.yml | 3744 | `de7d23d3fd688a09a8ecfe69acbe4e3a389c9ada7e67e47ec078697a9259611d` | `a3cafcd862bdcc5a276b311e36902a77ff9108b4` |
| results/R762-positive-meridian-arclength-and-two-coordinate-crown-fields.md | 13598 | `7c6efdceeee213993fed8bac7fb886e1fcada77e3eecbd183c9db836127070f8` | `a3ebdee5ee23dbb0903a9405a153d8903ebd4f91` |

workflow为 `.github/workflows/visible-larger-r762-gauged-crown-physical-fits.yml`，main上完整solver及workflow普通推送触发。此处发布时实际run/job/PID尚待原入口返回；未把提交或配置写成执行成功。

## 仍然未付与后续承接

R760的初始厚度结论只属于其明确初场。R760完整四路末端metric约 $10^5$，真新初帽修好了旧巨大内禀尖曲率，但并没有修好整个曲面的固定度量。R762固定开护领仍继承旧物理场，任何支持在其外的新增列都不能取消该领上的原残差；因此本实验的必要比较是把代理/坐标误差与真实物理不可动边界分开，不能以更细样条自动许诺 $10^{-6}$。

R764正在改成有真实曲率的较长预卷带，并释放公共圈和外围中央；R765另从曲率比与整面旋转可积条件构造。它们的目标g、边界自由度与论证各自重付。R762本次已登记的四条原预算完整完成后如失败即记录，不反复对已证不可能的护领原问题改名称重跑。完整任务仍是全闭C²、同g、全t厚度/held/商距及实际精化；未达到前持续。
