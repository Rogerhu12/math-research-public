# 同一物理终态的精确转移与跨中心范数方向记忆

日期：2026-11-15。状态：新源码和参数首发，全部新语法、接口人工和实际研究首次且仅在本公开仓库 GitHub Actions 执行。本文不预报改进或通过。

## 1. 已完成结果指出的具体费用

原 run 43728280256，job 132854922848，source 7329385a2dd84a40a271181c017c9a4028ae0f31 已完成。六个原模型、七次真实 trial、全部原始精确坐标、两个网格与新原始求值记录均已消费。其结果和限制见：

- [首次完整结果](complete-affine-first-actual-result-20261115.md)
- [六模型原式解释](complete-affine-six-model-interpretation-20261115.md)
- [恢复、SOC 与继续输入](complete-affine-restoration-and-resume-inputs-20261115.md)

原记录显示第4/5模型分别需要358/342条内层 norm cuts；第5模型的首个 LP 在完整仿射范数下没有正下降，补切平面后才出现可接受方向。第6模型只余一次 LP，停止不是驻点证据。与此同时，九个前序优化器恢复花费805.206121秒，新的实际部分35.287169秒。这里改变真正的提案算法，并从原精确物理终态直接进入；不延长原12个共享LP、40个共享完整值和120秒预算，不再次执行九个旧优化器或已付开发套件。

此次不能称旧优化状态完整恢复。对原426条JSON记录的已完成只读观察确认：精确159/163终态在日志，但后期完整行池列表和旧full-reference的全部切向向量没有输出。此事实保留，不能用池hash反演列表，不能自行填入“原池全部保留”。

## 2. 保存的对象及原范数支持不等式

原每个 soft row 的完整仿射函数为

$$
\varphi_\sigma(e,f)=\frac12\left(\sigma e+
\sqrt{e^2+4f^2+\epsilon^2}\right),\qquad \sigma\in\{1,-1\}.
$$

对任意真实单位球中的三向量 n，Cauchy–Schwarz 给对全部 e,f 同时成立的

$$
\ell_{\sigma,n}(e,f)
=\frac12\{(\sigma+n_1)e+2n_2 f+n_3\epsilon\}
\le\varphi_\sigma(e,f).
$$

因此可以保存原网格、原 flat row ID、原分支与 n，在新仿射中心重新代入原 e/f 和当前一阶导数。这个数学有效性不依赖旧、新中心接近；记忆方向不必仍是新中心的梯度。旧数值A/b则携带旧中心截距与旧trust尺度，不能原样搬来。

新中心写 e=e0+de·(Sz)、f=f0+df·(Sz)，原metric epigraph为rho，原target为m，新增行准确按

$$
A_{1:159}=
\left\{\frac{\sigma+n_1}{2}de+n_2df\right\}S,\quad
A_\rho=-1,\quad
b=m-\frac{\sigma+n_1}{2}e_0-n_2f_0-\frac12n_3\epsilon
$$

重建，其余原LP辅助列为零。始终使用当前中心、当前原J和当前S。若相同原点已在本模型selected点中，复用当前所需导数；否则只求该原点的新增行导数。两条分支共用点导数而保各自原flat ID和符号。

n从已观察的(e,2f,epsilon)方向取得。为防浮点归一化越出单位球，使用每个binary64分量的准确有理值核sum(n_i^2)≤1；若略越界，每次将三个分量用nextafter推向零，至多8次，超出则如实失败。每次装配还拒绝球外输入。这个准确单位球核不是整个浮点LP的区间证书；A/b装配、数值J与求解器仍按原浮点误差门，最终原完整值检查不可省。

## 3. 有界记忆与同一次原求解协议

记忆至多512个原行，采用每行最新方向、确定的FIFO淘汰。保存对象没有旧A/b，没有新网格ID，没有擅自生成的selected切平面。第一次记忆仅来自原完整日志的global directional attainer，其中明确保存了原ID、E/F和源中心hash；仅有cut点hash的其它原记录不被当作可恢复的方向。

每个新模型将记忆行加入第一次内层LP之前。后续selected/full-grid分离得到的新norm方向也进入同一个bank，供下一实际中心重建。complete affine oracle仍对原两完整网格扫描，额外cut生成和至多三次内层primary调用沿原逻辑；每个primary和SOC仍共用12调用账本。记忆本身不是完整网格扫描的替代品，也不把预测的新attainer直接加入实际硬门学习池。

原primary的A/b/information不修改。记忆行进入显式复制的当前cut LP，使原SOC仍看它原有的对象和规则。新outer是已冻结完整159 outer的一份明示源码分支：唯一数学调用替换为上述记忆primary；没有全局monkeypatch、没有在报告中虚称旧outer原函数实际被调用。

费用分别记录方向bank装配、复用/新增点J、完整方向扫描、LP、实际完整值、SOC以及最终两次独立复查。有限容量或有限预算停止不被命名为驻点、不可行或严格证书。

## 4. 从原精确159/163终态恢复同一物理族

原最后合格状态是模型5的SOC trial1、accepted_index5。原物理identity SHA256：

51f8ad73814080c9b2c20f8be92eba38bfb4081132ac1ac9144ecb8e7842c901

固定g：

fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6

固定b0：

d61fb298989834c9eb2b4fe3bbff1fb5983d1bb3b3980cb6441f14e6c0299bb5

读取原native精确列表时，对159个独立值必须逐项等于某个binary64的准确有理值。九个物理height不能先round为double。以原准确9×5矩阵H和原最后五个tau，用有理算术恢复

$$
h_{\mathrm{ref},j}
=h_{\mathrm{physical},j}
-\sum_{k=1}^{5}H_{jk}\tau_k .
$$

恢复的九个reference height逐项必须准确是binary64。新runtime full reference的前154项明确取当前切向系数；其九个height reference采用上述恢复。于是原仿射物理映射在全部159坐标上相同，不只在起点相同。重新求canonical物理identity、metric和b0的SHA必须全部核同。

原坐标definition含full-reference的物理tag。旧全部切向reference未输出，因此新tag如实不同。把新definition中的这一项替回原tag后，整个definition必须准确核回原b685021195473c8b1fede24bc27a90b105cf9ea327eeeb99933b68b78b1d9816。这同时约束其余全部H、height reference和layout内容；不称旧Python对象或缺失旧reference全向量恢复。

所有原lower/upper仍通过FiveNullHeightGate映射，起点和终点继续做准确原163盒检验。没有clipping，没有改变五height子空间，没有把163维物理族扩大。

## 5. 来源读取与明确的新行池

唯一原来源是上述已完成run/job的原日志。读取时核run/source/job/success、原10217369B日志SHA、3282055B原COMPLETE_REPORT子串SHA、原55785B receipt以及原106个源码文件。日志只在runner内存消费；redirect后的signed log host不带GitHub API credential。

原24输入只用已冻结growth.prepare_run做文件读入和已完成结果回放；不会调用其任何旧optimizer。所得coarse4414/fine3790旧输入行全部保留，并与原六模型中明确存在的全部合法grid/flat ID取并。该有限并集是**新池初始化**；明确不宣称包含未输出的后期全部旧池。若并集超过原不变容量则失败，不静默丢行或提高容量。

在该新池上按原当前状态初始化执行完整两网格学习。现有原hard gates、永久enriched c0、fine grid、box、SOC与acceptance保持原定义。初始完整值的eta/kappa与原最后两网格值比较，允许的数值差明确限5e-10，不强制其它漂移浮点hash等于旧偶然输出。

源controller准确继承B=.000125、success_streak0。原第6模型没有trial/反馈，不凭预算停创造一次成功或放大trust。原末次完结反馈来自模型5。

## 6. 首次新增开发范围

仅为新算法和缺失输入接口做新语义人工：

- binary64 normal的准确单位球及球外拒绝；
- 旧A/b在改变中心与trust后失效的明确反例，以及重建支持行两分支的保持；
- 原selected点复用与新增原行J、flat ID/branch与coordinate context边界；
- 512容量、同一原行最新方向和确定淘汰；
- 新seed行先进入第一LP，共享计数正确，原SOC primary对象未变；
- 带非二进有理H的精确height恢复，先round九物理值会改变输入的反例；
- 物理切向不一致及恢复出非binary64 reference时拒绝。

这些是尚未执行的新接口检查。不会跑旧complete oracle、旧SOC、旧profile或旧几何开发套件；既有数学门不作为新实验重复。

## 7. 首公开执行与输出

独立workflow visible-norm-memory-transfer.yml 由新request的push触发，与理论continuation请求互不覆盖。固定Python3.12.14、NumPy2.3.5、SciPy1.17.0，全部BLAS/OMP线程数1。

运行先实际git pull并比根/题README；有变只输出差异且在新研究前停供立即应用新规。另用已有MR_TOKEN在临时私有partial clone中实际pull，核两规则blob及唯一QUEUE进行中行，不输出私有内容。恢复GITHUB_SHA的科学源后，新五文件首次py_compile，然后新开发、精确物理转移、新实际求解与原两网格最终复核。

所有参数、原输入路径、原日志/receipt/物理身份和新源码hash在request中。新run、输出字节/SHA及人类实际结论另即时入log/results/HANDOFF。原日志、exact数组、bank、完整池和未来direct checkpoint只在runner临时文件及语义stdout；没有artifact/Release/机器证书提交。为免再次丢失后续恢复必要数据，本次stdout包含新reference精确向量、末态159/163、完整池和controller；它们绝不复制为仓库payload。

主任务仍无完成候选。采样eta、fine曲率58和有限box通过既不是全时metric≤1e−6，也不是reach≥.03D；当前τ.061要求曲率≤1000/61还需非局部reach。新算法只推进同g数值支线，不能把其辅助量叫成δhold。
