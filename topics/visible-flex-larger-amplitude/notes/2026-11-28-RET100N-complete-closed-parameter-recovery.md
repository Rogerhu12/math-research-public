# RET100N — 已终止分支完整参数逐字恢复与容量登记

会话 Astra-larger-e4e2a2bf-20261126。此项只处理原已终止分支的完整准备参数和七份队列，不产生或替代任何科学计算。完整登记：[恢复manifest](../computations/ret100n-closed-actions-whole-parameter-recovery.json)，[原来源和官方终态](../computations/ret100n-frozen-scope-and-closed-job-identities.json)，[独立复原程序](../computations/reproduce_ret100n_closed_actions_full_parameters.mjs)。原完整 Git 树固定为 `e6e134d429ec951c2c028579ade98229e38c34cb`，可直接获取每一原文。

ROOT独立读了61份完整父JSON和9份完整编辑文，保原空白、键序、数值字面量和标点。每一复制区间只引用编号严格更早的另一整件，不以被恢复文件自身为父，不跨编辑文件拆一原文。独立复原111/111份完整原参数，均成功解析为完整JSON，且各自UTF-8字节数、SHA256和Git blob三项身份完全一致；合计3158155字节。111件的完整身份和分支对应见manifest。复原只做文本与身份检查，没有加载科学程序、数组或重算旧结论。

ROOT另独立读取198份保护清单完整源文及参数（185基础件加13个R766/R769/R770/R772和当前atlas输入），每件三项身份一致，未发现任何被退件 basename 引用。一次run41请求读取暂未返回，随后完整重取18364B并验得 `0012caaefde888f2ce874cc180042f5090cbe792`，未略过。runtime另核了198个相关workflow的push头，未发现此次删除触发或通配命中；不删除任何现有workflow触发请求。

ROOT直接读取登记的27个官方run与27个jobs，逐个比较run/attempt/head/status/conclusion及job身份，全部为原对应终态。官方完成、失败或取消只证明那个job终止，不证明其中每一准备步骤已执行，尤其不把未返回science/pure算作已有结果。具体官方身份和时间全保scope登记；旧实际观察、失败点、未知责任和数学结论均原样保留。

12份新完整恢复件共790414B，替换的111份旧准备件3158155B，恢复包本身净释放2367741B；本条说明和导航/日志另计。61份独立父完整保留。R732的19/20原父、活输入、完整科学源、原工作流请求、先前恢复依赖、唯一返回值、原预算、完整实际返回与所有未付研究标准均不属于此次退件。

复现命令：

```sh
node topics/visible-flex-larger-amplitude/computations/reproduce_ret100n_closed_actions_full_parameters.mjs OUTPUT_DIRECTORY
```

程序从固定历史整树取每份父文，验证全部父与编辑文件身份，再逐件重建并验证每个完整输出。现有输出只在三项身份仍完全一致时接受，未返回或身份不同会报错。公开科学执行仍只在原授权Actions，科研完成标准没有改变。
